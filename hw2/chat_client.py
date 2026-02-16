from __future__ import annotations
from abc import ABC, abstractmethod

# Why use Strategy

# strategy interface
class Mode(ABC):
    @abstractmethod
    def transform_message(self, message: str) -> str:
        """Return a transformed message"""
        raise NotImplementedError

# concrete strategies
class PlainText(Mode):
    def transform_message(self, message: str) -> str:
        processed = message
        return processed

    def __str__(self):
        return "PLAIN"

class Encrypted(Mode):
    def transform_message(self, message: str) -> str:
        processed = message[::-1]
        return processed

    def __str__(self):
        return "ENCRYPTED"

class Compressed(Mode):
    def transform_message(self, message: str) -> str:
        processed = "".join(ch for ch in message if ch.lower() not in "aeiou")
        return processed

    def __str__(self):
        return "COMPRESSED"

class Vowels(Mode):
    def __str__(self):
        return "COMPRESSED"


# context
class ChatClient:
    def __init__(self) -> None:
        self._mode: Mode = PlainText()

    def set_mode(self, mode: Mode) -> None:
        self._mode = mode

    def send(self, message: str) -> str:
        processed = self._mode.transform_message(message)
        print(f"[SEND] mode={self._mode} \t payload={processed}")
        return processed


def main() -> None:
    client = ChatClient()

    client.send("Hello World")

    client.set_mode(Encrypted())
    client.send("Hello World")

    client.set_mode(Compressed())
    client.send("Hello World")


if __name__ == "__main__":
    main()
