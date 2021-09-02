#Quran-Anki-Project

A script to pull json from Quran.com api as well as a script to convert those objects into csv files by page so that we can import them into Anki for study. 

Pages has two folders /json & /csv. JSON is a direct page from the API. CSV is just the fields of interest. This can be refactored to take out the csv step. 
Json are the files pulled directly from https://quran.api-docs.io/v4/verses/by-page (Thanks Naveed). 


##Background
I am in the habit of using Anki for my classes and I would like to use Anki to memorize the definitions of the words of the Quran as I begin my journey to memorize the Quran Al Majeed, by the Will of Allah (Swt).

##Goal

My goal is to create an Anki collection of decks for each word (Arabic/English) and Arabic Audio for each word in the Quran.


My intention is to use a program (in any language [node,python,java] ) to create 604 Decks, one for each page of the Quran Al Majeed. This way I can learn Deck at a time therfore enabling me to learning one page at a time. Each card will 4 fields. Here is an example of two lines.

"Page Number", "Arabic Word", "English Word", "URL to Arabic Audio",
"604","قُلْ","Say", "https://audio.qurancdn.com/wbw/114_001_001.mp3"



##Notes
- sandbox files are for experimentation. 
- python is running in an anaconda env, so you will need to setup an environment to run it. 
- node just needs the npm -i; although you will need python to actually build the decks. Python also pulls the media files. 
- Anki appears to have a limit per user of 25k cards. There are 78k words in the Quran with reversibility this amounts to 156k cards. I removed redundancy per page but left redundancy across the collection. This brought the words down to 67.5K which transposes to 135k cards. 
- Theories to simplify: I can create different shared decks based on Juz 30 (135k/30=4.5K cards), Hizb 60 (135k/60=2.25K cards), Rub 240 (135k/240=.56K cards); I think I'll group them in 5 Juz at a time. This should manifest around 22k cards per collection. 
- Audio files add up to around 6GB. Cards alone add up to around 100MB. 
- the decks in Github DO NOT HAVE AUDIO. 