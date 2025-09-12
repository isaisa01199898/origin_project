from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyAi541WuxVD8ZMb2YalkjCS90bjG2MspMk") # あなたのAPIキー

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-tts",
    contents="こんにちは",
    config=types.GenerateContentConfig(response_modalities=['AUDIO']) # ★ここが重要★
)

print(response) # レスポンスの中身を確認

if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
    with open("C:\\Users\\isami\\OneDrive\\Desktop\\myproject\\output.mp3", "wb") as f:
        f.write(response.candidates[0].content.parts[0].inline_data.data) # ★ここも重要★
else:
    print("音声データが取得できませんでした")
import wave

audio_data = response.candidates[0].content.parts[0].inline_data.data

with wave.open("output.wav", "wb") as wf:
    wf.setnchannels(1)         # モノラル
    wf.setsampwidth(2)         # 16bit = 2byte
    wf.setframerate(24000)     # 24kHz
    wf.writeframes(audio_data)