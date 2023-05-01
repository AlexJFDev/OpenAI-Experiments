# Used Imports
import openai
import os
import time
from dotenv import load_dotenv
from Logger import Logger
from Conversation import Conversation
from Message import Message

# Type Imports
from typing import IO, Any

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def continue_conversation(conversation: Conversation) -> Any:
    conversation_str: str = conversation.get_str()

    response = openai.Completion.create( # type: ignore
        model="text-davinci-003",
        prompt=conversation_str,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.5
    )

    response_text: str = response.choices[0].text # type: ignore

    try:
        role, content = response_text.split(":") # type: ignore
        conversation.append(Message(role, content)) # type: ignore
        return(response) # type: ignore
    except ValueError:
        print("Got unexpected output.")
        conversation.append(Message("", response_text)) # type: ignore
        return(response) # type: ignore

conversation = Conversation(
    Message("Alex", "Hello, my name's Alex! What's yours?"),
    Message("Bert", "Hello, Alex! My name is Bert! How are you doing?"),
    Message("Alex", "Nice to meet you Bert. I'm doing good. How about yourself?"),
    Message("Bert", "I'm fine thank you. What are your hobbies?"),
    Message("Alex", "I love playing sports and video games, reading, and watching movies. How about you?"),
    Message("Bert", "I enjoy playing sports, reading, watching movies, and going on hikes."),
    Message("Alex", "That's really cool. What sports do you play?"),
)

print("""This script uses OpenAI's completion models to simulate conversation.
Whenever you press enter the API will be called with the current conversation and the output will be printed to stdout and a log file. If you do something other than enter the program will stop.
--------
The starting conversation is below:""")

current_time: str = time.strftime("%Y-%m-%d,%H_%M_%S")
conversation_log_name: str = f"logs/completion/conversation-{current_time}.ai-log"
detailed_log_name: str = f"logs/completion/detailed-{current_time}.ai-log"
conversation_log = Logger(conversation_log_name)
detailed_log: IO[Any] = open(detailed_log_name, "w")

conversation_log.write(conversation.get_str(), end="")

while True:
    if input(""): break
    response: Any = continue_conversation(conversation)
    conversation_log.write(response.choices[0].text)
    detailed_log.write(str(response))
detailed_log.close()
conversation_log.close()
