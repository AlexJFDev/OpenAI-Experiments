from Message import Message

class Conversation:
    def __init__(self, *messages: Message, message_list: list[Message] = []) -> None:
        self.message_list: list[Message] = []
        for message in messages:
            self.message_list.append(message)
        for message in message_list:
            self.message_list.append(message)

    def get(self, message_num: int) -> Message:
        return self.message_list[message_num]

    def append(self, message: Message) -> None:
        self.message_list.append(message)
    
    def get_str(self) -> str:
        conversation_str: str = ""
        for message in self.message_list:
            conversation_str += message.get_str()
        return conversation_str
    
    @classmethod
    def from_str(cls, str_conversation: str):
        conversation_str_list: list[str] = str_conversation.split("\n")
        message_list: list[Message] = []
        for message in conversation_str_list[:-1]:
            role, content = message.split(":")
            message_list.append(Message(role, content))
        return cls(message_list=message_list)
        
            