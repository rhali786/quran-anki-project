#Quran-Anki-Project

A script to pull json from Quran.com api as well as a script to convert those objects into csv files by page so that we can import them into Anki for study. 

Pages has two folders /json /csv
Json are the files pulled directly from https://quran.api-docs.io/v4/verses/by-page (Thanks Naveed). 
/csv are the files necessary to construct the Anki decks. 


I am in the habit of using Anki for my classes and I would like to use Anki to memorize the definitions of the words of the Quran as I begin my journey to memorize the Quran Al Majeed, by the Will of Allah (Swt).


My goal is to create an Anki collection of decks for each word (Arabic/English) and Arabic Audio for each word in the Quran.

My intention is to use a program (in any language [node,python,java] ) to create 604 csv spreadsheets, one for each page of the Quran Al Majeed. This way I can learn one csv at a time thus learning one page at a time. Each page will have a comma separated line with 4 fields. Here is an example of two lines.

"Page Number", "Arabic Word", "English Word", "URL to Arabic Audio",
"604","قُلْ","Say", "https://audio.qurancdn.com/wbw/114_001_001.mp3"

So the challenge is to figure out how to iterate through the api and produce these 4 fields for each page and each word in the Quran.

If you are interested in trying we can work together, but I can also hire someone to do it. I know I'm busy and I'm sure you are as well. I don't know how much to pay for a project like this. If I had someone create these manually I was going to pay $1 per page and ask for 20-40 pages per month.