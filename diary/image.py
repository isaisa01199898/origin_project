from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client(api_key="AIzaSyCcDqS18vRebeRB8t8f4s-i8kFYElq_m1I")


contents = ('色々教えて')

response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
    response_modalities=['TEXT']
    )
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO((part.inline_data.data)))
        image.save('C:/Users/isami/OneDrive/Desktop/myproject/diary/static/diary/ground.png')
        image.show()