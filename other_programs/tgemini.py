import google.generativeai as genai
from google.genai import types
from PIL import Image
from google import genai
from io import BytesIO


client = genai.Client(api_key="AIzaSyCcDqS18vRebeRB8t8f4s-i8kFYElq_m1I")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f'WROについて教えてください',
)
message = response.text
print(message)

contents = ("WROのFIのイメージ画像を生成してください")  #画像を生成するためのプロンプト

client = genai.Client(api_key="AIzaSyCcDqS18vRebeRB8t8f4s-i8kFYElq_m1I")

response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",  #モデルの指定
    contents=contents,
    config=types.GenerateContentConfig(
    response_modalities=["IMAGE", "TEXT"]
    )
)

for part in response.candidates[0].content.parts:
    if part.inline_data is not None:
        image = Image.open(BytesIO((part.inline_data.data)))
        image.save('C:/Users/isami/OneDrive/Desktop/myproject/diary/static/diary/ground_v3.0.png')
        image.show()