import google.generativeai as genai
client = genai.Client(api_key="APIキーを入れる")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f'プロンプトを入力',
)
message = response.text
print(message)#帰ってきたメッセージ
