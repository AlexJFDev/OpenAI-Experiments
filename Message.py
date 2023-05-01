class Message:
    def __init__(self, _role: str, _content: str) -> None:
        self.role: str = _role
        self.content: str = _content

    def get_str(self) -> str:
        return f"{self.role}:{self.content}\n"