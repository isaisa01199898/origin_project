
import gtts
from gtts import gTTS
text = "集中力がなくなってきているね、こんな名言があるのしってる？"
tts = gTTS(text=text, lang='ja',slow=False)
tts.save("C:/Users/isami/OneDrive/Desktop/myproject/diary/static/diary/out.mp3") 
bg_image = 'diary/white.png'
bg_image = 'diary/ground_v5.0.png'