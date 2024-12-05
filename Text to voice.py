from gtts import gTTS
import os

language = "en"

text= input("TEXT HRER :")
voice = gTTS(text=text, lang=language, slow=False)

voice.save("voice.mp3")
