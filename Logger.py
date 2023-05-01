# Used Imports
import sys
import os

# Type Imports
from typing import IO, Any

class Logger:
    def __init__(self, _log_path: str, mode: str = "w") -> None:
        self.log_path: str = _log_path
        os.makedirs(os.path.dirname(_log_path), exist_ok=True)
        self.log_file: IO[Any] = open(_log_path, mode)
    
    def write(self, message: Any, end: str = "\n") -> None:
        message_str: str = str(message)
        sys.stdout.write(f"{message_str}{end}")
        self.log_file.write(f"{message_str}{end}")

    def close(self) -> None:
        self.log_file.close()