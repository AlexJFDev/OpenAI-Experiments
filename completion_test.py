# Used Imports
import openai
import os
import time
from dotenv import load_dotenv
from Logger import Logger
from Conversation import Conversation
from Message import Message

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def continue_conversation(conversation: Conversation) -> str:
    conversation_str: str = conversation.get_str()

    response = openai.Completion.create( # type: ignore
        model="text-davinci-003",
        prompt=conversation_str,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.5,
        stop=["\n"]
    )

    response_text: str = response.choices[0].text # type: ignore

    try:
        role, content = response_text.split(":") # type: ignore
        conversation.append(Message(role, content)) # type: ignore
        return(response_text) # type: ignore
    except ValueError:
        print("got unexpected output")
        conversation.append(Message("", response_text)) # type: ignore
        return(response_text) # type: ignore

conversation = Conversation(
    Message("Alex", "Hello, my name's Alex! What's yours?"),
    Message("Bert", "Hello, Alex! My name is Bert! How are you doing?"),
    Message("Alex", "Nice to meet you Bert. I'm doing good. How about yourself?"),
    Message("Bert", "I'm fine thank you. What are your hobbies?"),
    Message("Alex", "I love playing sports and video games, reading, and watching movies. How about you?"),
    Message("Bert", "I enjoy playing sports, reading, watching movies, and going on hikes."),
    Message("Alex", "That's really cool. What sports do you play?"),
)

print("This script uses OpenAI's completion models to simulate conversation.\nWhenever you press enter the API will be called with the current conversation and the output will be printed to Stdout and a log file. If you do something other than enter the program will stop.\n--------\nThe starting conversation is below:")

current_time: str = time.strftime("%Y-%m-%d,%H_%M_%S")
file_name: str = f"logs/completion/{current_time}.ai-log"
log = Logger(file_name)
log.write(conversation.get_str(), end="")

while True:
    if input(""): break
    response = continue_conversation(conversation)
    log.write(response)
log.close()
