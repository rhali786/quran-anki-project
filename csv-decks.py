import csv
import random
import genanki
import os
import datetime
import requests
import sys 

# Create the deck model
model_id = random.randrange(1 << 30, 1 << 31)
css = """
    .card {
 font-family: -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;
 font-size: 2em;
 background-color: #fafafa;
 max-width: 40rem;
 padding: 2rem;
 margin: auto;
 color: #222;
 }
center {
    text-align: center;
    }"""
templates=[
        {
            "name": "Arabic Word",
            "qfmt": '<h1>{{Arabic}} {{audio}}</h1>',
            "afmt": '{{FrontSide}}<hr id="answer"><h1>{{English}} </h1><center>{{Ayat}}</center>',
        },
        {
            "name": "English Word",
            "qfmt": '<h1>{{English}}</h1>',
            "afmt": '{{FrontSide}}<hr id="answer"><h1>{{Arabic}} {{audio}}</h1><center>{{Ayat}}</center>',
        },
    ]
fields=[{"name": "Arabic"}, {"name": "English"}, {"name": "audio"}, {"name": "Ayat"}]
anki_model_name = "100% Quran.com"
anki_model = genanki.Model(model_id,anki_model_name, fields, templates,css)


directory = "pages/csv/"
current_time = datetime.datetime.now()
for filename in os.listdir(directory):
    if filename=="-Page_101_Juz_5_Hizb_10_Rub_40.csv": #erase the dash to limit the decks made
         break
    else:
        anki_notes = []
        anki_deck_title = filename.split(".")[0]
        deck_filename = anki_deck_title+".apkg"
        audio_files = [] #to be added to package
        unqiue_words = [] # to reduce duplicate words

        with open(directory+ filename, "r",encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
        
            rowCount = 0
            audio_count = 0 
            for row in csv_reader:
                rowCount = rowCount+1

                #reduce same words in same deck; or page number
                if row[0] == "'Page Number'" or row[1] in unqiue_words:
                    #print(str(rowCount)+"!!"+ row[1])
                    continue
                unqiue_words.append(row[1])
            
                #Download media file
                audio_url = row[3].strip("'")
                audio_file = audio_url.split('/')[-1]
                audio_file_location = 'mp3s/'+audio_file
                audio_files.append(audio_file_location)

                #if file exists skip else get and save and count
                if  not os.path.isfile(audio_file_location): 
                    session = requests.Session()
#                    response = requests.get(audio_url, headers={'User-Agent': 'Mozilla/5.0'})
#                    open(audio_file_location, 'wb').write(response.content)
                    #sys.stdout.write(audio_file) #for logging row number of mp3 downloaded
                    audio_count = audio_count+1

                anki_note = genanki.Note(
                    model=anki_model,
                    # simplified writing, pinyin, meaning
                    fields=[row[1].strip("'"),row[2].strip("'"),"[sound:%s]"%audio_file,row[4].strip("'")], 
                )
                anki_notes.append(anki_note)

            anki_deck = genanki.Deck(model_id, anki_deck_title)
            anki_package = genanki.Package(anki_deck)
#            anki_package.media_files = audio_files
        
            # Add flashcards to the deck
            for anki_note in anki_notes:
                anki_deck.add_note(anki_note)

            # Save the deck to a file
            anki_package.write_to_file("decks/"+ deck_filename)


        print("%s : Created %s with %d flashcards and %d new / %d total Audio Files"% (datetime.datetime.now() - current_time,deck_filename, len(anki_deck.notes),audio_count, len(audio_files)))