from __future__ import annotations
from abc import ABC, abstractmethod
from base64 import b64encode

# Why I chose the Strategy Pattern
"""
Problems with original implementation:
    1. What are the design problems with ChatClient?
        - The client doesnt need to know what algorithm we are using to modify the message
        - It exposes our algorithms we use on the message
    2. Why does the use of conditionals make the code hard to extend and maintain?
        - When we need to add any new ways of sending a messages, we have to add another if statement inside the send method.
        - Any changes, modifications, or variations made have to occur in the main class
        - Any bugs would be difficult to troubleshoot

Problems with State for our use case:
    1. The state model is used when the object itself is changing, but in our case it is not the client object but the *message* that is changing.
    2. The class behavior (ChatClient) does not depend on a state, it will send messages the same way for each message transformation type.

Why Strategy works:
    1. We are always doing the same task, sending a message, we just want to do this task in different ways. 
    2. We can replace the many behaviors (all the ifs / conditionals) by moving behavior specific strategies into individual classes. 
    3. Now we no longer need those conditionals, and the client or user can simply select the desired behavior. 

Therefore, it is more appropriate for the user to select a 'strategy' for how to manipulate the message.

Additionally, we can easily add more classes (see my Base64 example) to extend the features of the chat client. 
"""

# strategy interface
class Mode(ABC):
    @abstractmethod
    def transform_message(self, message: str) -> str:
        """Return a transformed message"""
        raise NotImplementedError

# concrete strategies
class PlainText(Mode):
    # no modifications made
    def transform_message(self, message: str) -> str:
        processed = message
        return processed

    def __str__(self) -> str:
        return "PLAIN"

class Encrypted(Mode):
    # sends in reverse, could swap for a real encryption algorithm later on
    def transform_message(self, message: str) -> str:
        processed = message[::-1]
        return processed

    def __str__(self) -> str:
        return "ENCRYPTED"

class Compressed(Mode):
    # compresses by removing vowels
    def transform_message(self, message: str) -> str:
        processed = "".join(ch for ch in message if ch.lower() not in "aeiou")
        return processed

    def __str__(self) -> str:
        return "COMPRESSED"

class Base64(Mode):
    # converts the message to a base64 string
    def transform_message(self, message: str) -> str:
        # the base64 method doesn't work with a string, I had to convert it to a "bytes-like object" using encode()
        # however, this returns as a bytes object, and I want a string, so I had to then use decode()
        # https://stackoverflow.com/questions/7585435/how-to-convert-string-to-bytes-in-python-3
        processed_bytes = b64encode(message.encode())
        processed = processed_bytes.decode()
        return processed

    def __str__(self) -> str:
        return "BASE64"

# context
class ChatClient:
    # init with default mode of PlainText()
    def __init__(self, mode: Mode = PlainText()) -> None:
        self._mode = mode

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

    client.set_mode(Base64())
    client.send("Hello World")


if __name__ == "__main__":
    main()
