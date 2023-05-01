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

messages: list[dict[str, str]] = [{'role': 'user', 'content': "Hello, my name's Alex! What's yours?"},
 {'role': 'assistant', 'content': 'Hello, Alex! My name is Bert! How are you doing?'},
 {'role': 'user', 'content': "Nice to meet you Bert. I'm doing good. How about yourself?"},
 {'role': 'assistant', 'content': "I'm fine thank you. What are your hobbies?"},
 {'role': 'user', 'content': "As an AI language model, I don't have hobbies like humans do, but I'm here to answer your questions and help you in any way I can. How can I assist you today?"},
 {'role': 'assistant', 'content': "Oh, I apologize for my mistake. As you mentioned that you're here to assist me, can you tell me more about yourself? What can you do?"},
 {'role': 'user', 'content': "Of course! I am an AI language model capable of understanding natural language and providing human-like responses to various queries. I can answer questions related to a wide range of topics such as general knowledge, math, science, history, and more. I can also assist with tasks such as writing articles, composing emails, and even conducting research. Is there anything specific you'd like me to help with?"},
 {'role': 'assistant', 'content': 'Actually, yes. Can you explain to me the importance of cybersecurity in our digital world?'}]
role_num: int = 0
while True:
    if input("enter to continue"): break
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages = messages
    )

    role: str = roles[role_num] # chat.choices[0].message.role
    content: str = chat.choices[0].message.content

    print(f"{role}: {content}")
    messages.append({"role": role, "content":content})

    role_num = (role_num + 1) % 2

cur_time: str = time.strftime("%Y-%m-%d,%H_%M_%S")
file_name: str = f"logs/{cur_time}.ai-log"
file: TextIOWrapper = open(file_name, "w")
file.write(str(messages).replace("},", "},\n"))
file.close()
print(messages)