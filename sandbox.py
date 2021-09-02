import urllib.request 
import requests


#urllib.request.urlretrieve("http://www.google.com", "home.html")
audio_file = str.split('/')[-1]
str = 'https://audio.qurancdn.com/wbw/004_135_002.mp3'



session = requests.Session()
response = requests.get(str, headers={'User-Agent': 'Mozilla/5.0'})
open('sound.mp3', 'wb').write(response.content)


#webpage = urlopen(req).read()
#urllib.request.urlretrieve(str, "mp3s/"+audio_file)
