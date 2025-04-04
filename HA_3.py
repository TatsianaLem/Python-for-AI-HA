from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

model_name = "gemini-2.0-flash"
prompt = "Опиши кошку в нескольких предложениях, каждое предложение с новой строки "

response = client.models.generate_content(
    model=model_name,
    contents=prompt
)

print(response.text)
