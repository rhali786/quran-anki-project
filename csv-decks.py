import csv
import random
import genanki
import os
import datetime
import urllib.request 



#-----------------------------------------------------------------------------------
"""

add media

""" 
#-----------------------------------------------------------------------------------

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
            "qfmt": '<h1>{{Arabic}}</h1>',
            "afmt": '{{FrontSide}}<hr id="answer"><h1>{{English}} {{audio}}</h1><center>{{Ayat}}</center>',
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
    if filename=="-Page_102_Juz_6_Hizb_11_Rub_41.csv": #erase the dash to limit the decks made
         break
    else:
        anki_notes = []
        anki_deck_title = filename.split(".")[0]
        deck_filename = anki_deck_title+".apkg"

        with open(directory+ filename, "r",encoding="utf8") as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=",")

            for row in csv_reader:
                if row[0] == "'Page Number'":
                    continue
                
                #Download media file
                audio_url = row[3].strip("'")
                audio_file = audio_url.split('/')[-1]

                #urllib.request.urlretrieve(audio_url, "mp3s/"+audio_file)
                
                anki_note = genanki.Note(
                    model=anki_model,
                    # simplified writing, pinyin, meaning
                    fields=[row[1].strip("'"),row[2].strip("'"),"[sound:%s]"%audio_file,row[4].strip("'")], #TODO::ASDFASDFASDFASDAFASDFASFADSFTODO TODO TODO
                )
                anki_notes.append(anki_note)

        anki_deck = genanki.Deck(model_id, anki_deck_title)
        anki_package = genanki.Package(anki_deck)
        
        # Add flashcards to the deck
        for anki_note in anki_notes:
            anki_deck.add_note(anki_note)

        # Save the deck to a file
        anki_package.write_to_file("decks/"+ deck_filename)

        print("%s : Created %s with %d flashcards"% (datetime.datetime.now() - current_time,deck_filename, len(anki_deck.notes)))