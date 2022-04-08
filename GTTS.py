from datetime import date
from gtts import gTTS
import os
from langdetect import detect


def stab(arr):
    word = arr[0]
    while(len(word) < 15):
        word += " "
    word += " | " + arr[1]
    return word


dic = []
date = date.today().strftime('%Y-%m-%d')
with open("Speechwords.txt", "r+", encoding="utf-8") as file:
    arr = file.readlines()
    for i in arr:
        parsed = i.split("-")
        dic.append({"en": parsed[0], "tr": parsed[1].split("\n")[0]})
fileName = arr[0].split("-")[0]
counter = len(dic)
try:
    os.mkdir(os.path.join("./wordsANDsounds", f'{date}({fileName})'))
except:
    pass
with open(f'wordsANDsounds/{date}({fileName})/{date}({fileName}).txt', 'w+', encoding="utf-8") as f:
    for i in arr:
        parsed = i.split("-")
        text = stab(parsed)
        print(text)
        f.write(text)
with open(f'wordsANDsounds/{date}({fileName})/{date}({fileName}).mp3', 'wb') as f:
    for i in dic:
        print(f'{counter} - {i["en"]}')
        counter -= 1
        tts_en = gTTS(i["en"], lang='en')
        tts_en.write_to_fp(f)
        parsedMean = i["tr"].split(",")
        for x in parsedMean:
            try:
                if(detect(x) == "en"):
                    tts_en = gTTS(x, lang='en')
                    tts_en.write_to_fp(f)
                else:
                    tts_tr = gTTS(x, lang='tr')
                    tts_tr.write_to_fp(f)
            except:
                continue
