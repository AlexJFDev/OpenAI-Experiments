# Used Imports
import openai
import os
import time
from dotenv import load_dotenv

# Type Imports
from io import TextIOWrapper
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def conversation_to_str(conversation: list[dict[str, str]]) -> str:
    conversation_str: str = ""
    for message in conversation:
        role: str = message.get("role")
        content: str = message.get("content")
        conversation_str += f"{role}:{content}\n\n"

    return conversation_str

def continue_conversation(conversation: list[dict[str, str]]) -> None:
    conversation_str: str = conversation_to_str(conversation)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation_str,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.5,
        stop=["\n"]
    )
    response_text: str = response.choices[0].text
    print(response_text)
    try:
        role, content = response_text.split(":")
        conversation.append({"role": role, "content": content})
    except ValueError:
        print("got unexpected output")
        conversation.append({"role": "", "content": response_text})
    

starting_conversation: list[dict[str, str]] = [
    {"role": "Alex", "content": "Hello, my name's Alex! What's yours?"},
    {"role": "Bert", "content": "Hello, Alex! My name is Bert! How are you doing?"},
    {"role": "Alex", "content": "Nice to meet you Bert. I'm doing good. How about yourself?"},
    {"role": "Bert", "content": "I'm fine thank you. What are your hobbies?"}
]

print(conversation_to_str(starting_conversation), end="")

while True:
    if input("enter to continue"): break
    continue_conversation(starting_conversation)

cur_time: str = time.strftime("%Y-%m-%d,%H_%M_%S")
file_name: str = f"logs/{cur_time}.ai-log"
file: TextIOWrapper = open(file_name, "w")
file.write(str(starting_conversation).replace("},", "},\n"))
file.close()
print(starting_conversation)