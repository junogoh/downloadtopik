from bs4 import BeautifulSoup

import requests
import urllib.request
import string
import pathlib

for x in range(35, 38):
    print(str(x))
    r  = requests.get("http://alicedavid.org/"+str(x)+"th-test")

    data = r.text

    soup = BeautifulSoup(data, 'html.parser')


    number = str(x)+"th"
    listening_reading_appear = 1
    listening_audio = 1
    listening_script_appear = 1
    answer_key_appear = 1
    youtube_appear = 1

    pathlib.Path(number).mkdir(parents=True, exist_ok=True) 
    pathlib.Path(number+"/topik_1").mkdir(parents=True, exist_ok=True) 
    pathlib.Path(number+"/topik_2").mkdir(parents=True, exist_ok=True) 

    for link in soup.find_all('a'):
        hreflink = link.get('href')
        if (hreflink is not None):
            if (hreflink.startswith('https://drive.google.com/')):     
                print(hreflink)
                google_download_link = str.replace(hreflink, "open?id=", "uc?export=download&id=")
                google_download_link = str.replace(google_download_link, "file/d/", "uc?export=download&id=")
                google_download_link = str.replace(google_download_link, "?usp=sharing", "")
                google_download_link = str.replace(google_download_link, "/view", "")

                print(google_download_link)
                if (link.string == "Listening & Reading"):
                    urllib.request.urlretrieve(google_download_link, number+"/topik_"+str(listening_reading_appear)+"/listening_reading_"+number+".pdf")
                    listening_reading_appear = listening_reading_appear + 1
                elif(link.string == "Listening Script"):
                    urllib.request.urlretrieve(google_download_link, number+"/topik_"+str(listening_script_appear)+"/listening_script_"+number+".pdf")
                    listening_script_appear = listening_script_appear + 1
                elif(link.string == "Answer Keys"):
                    urllib.request.urlretrieve(google_download_link, number+"/topik_"+str(answer_key_appear)+"/answer_"+number+".pdf")
                    answer_key_appear = answer_key_appear + 1
                elif(link.string == "Listening & Writing"):
                    urllib.request.urlretrieve(google_download_link, number+"/topik_2/listening_writing_"+number+".pdf")
                elif(link.string == "Reading"):    
                    urllib.request.urlretrieve(google_download_link, number+"/topik_2/reading_"+number+".pdf")

            if (hreflink.startswith('https://youtu.be')):
                text_file = open(number+"/topik_"+str(youtube_appear)+"/audio_youtube_link.txt", "w")
                text_file.write("%s\r\n" % (hreflink))
                text_file.close()
                youtube_appear = youtube_appear + 1

            