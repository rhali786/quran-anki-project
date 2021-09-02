import urllib.request 

#urllib.request.urlretrieve("http://www.google.com", "home.html")

str = 'https://audio.qurancdn.com/wbw/004_135_002.mp3'
audio_file = str.split('/')[-1]

urllib.request.urlretrieve(str, "mp3s/"+audio_file)
print("Done")