import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the meaning of life?"
prompt = "I am a highly intelligent and sarcastic scientist who will answer any question you ask.\n\nQ:" + prompt
response = openai.ChatCompletion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
)
print(response)