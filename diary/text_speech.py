# from gtts import gTTS
# import os

# text = "さあ、始まりました！（テンション高く発音）"
# tts = gTTS(text=text, lang='ja')
# tts.save("C:/Users/isami/OneDrive/Desktop/myproject/diary/static/diary/output.mp3")
import pyttsx4

engine = pyttsx4.init()
engine.save_to_file('さあ、文化祭が始まりました!', 'C:/Users/isami/OneDrive/Desktop/myproject/diary/static/diary/test.mp3')
engine.runAndWait()
