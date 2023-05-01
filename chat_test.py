# Used Imports
import openai
import os
import time
from dotenv import load_dotenv

# Type Imports
from io import TextIOWrapper

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

roles: list[str] = ["user", "assistant"]

messages: list[dict[str, str]] = [
    {"role": "user", "content": "Hello, my name's Alex! What's yours?"},
    {"role": "assistant", "content": "Hello, Alex! My name is Bert! How are you doing?"},
    {"role": "user", "content": "Nice to meet you Bert. I'm doing good. How about yourself?"},
    {"role": "assistant", "content": "I'm fine thank you. What are your hobbies?"},
]
role_num: int = 0
while True:
    if input("enter to continue"):
        break
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages = messages
    )

    role: str = roles[role_num] # chat.choices[0].message.role
    content: str = chat.choices[0].message.content

    print(f"{role}: {content}")
    messages.append({"role": role, "content":content})

    role_num = (role_num + 1) % 2

print(str(messages).replace("},", "},\n"))

cur_time: str = time.strftime("%Y-%m-%d,%H_%M_%S")
file_name: str = f"logs/{cur_time}.ailog"
file: TextIOWrapper = open(file_name, "w")
file.write(str(messages).replace("},", "},\n"))
file.close()
print(messages)