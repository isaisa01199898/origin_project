
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
client = genai.Client(api_key="AIzaSyAi541WuxVD8ZMb2YalkjCS90bjG2MspMk")

contents = (f"ドラマ「ドラゴン桜」の桜木先生の画像を生成してください周りに桜を演出して（ちなみにhttps://dragonzakura.mitanorifusa.com/img/chara-img-01.jpg、の画像を必ず参考にして生成して）（サイズは1:1で）")  #画像を生成するためのプロンプト

response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",  #モデルの指定
    contents=contents,
    config=types.GenerateContentConfig(
    response_modalities=['TEXT','IMAGE']
    )
)


#13
for part in response.candidates[0].content.parts:
    if part.inline_data is not None:
        image = Image.open(BytesIO((part.inline_data.data)))
        image.save('C:/Users/isami/OneDrive/Desktop/myproject/diary/static/diary/ground_v5.0.png')
        image.show()  # 画像を表示

