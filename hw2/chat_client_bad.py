from __future__ import annotations
from enum import Enum


class Mode(Enum):
    PLAIN = "plain"
    ENCRYPTED = "encrypted"
    COMPRESSED = "compressed"


class ChatClient:
    """
    INTENTIONALLY BAD DESIGN:
    - Big if/elif grows with every new mode
    - Message processing + sending are tangled together
    - Adding a new mode requires editing this class (not extensible)
    - Harder to test each behavior in isolation
    """

    def __init__(self) -> None:
        self._mode: Mode = Mode.PLAIN

    def set_mode(self, mode: Mode) -> None:
        self._mode = mode

    def send(self, message: str) -> str:
        if self._mode is Mode.PLAIN:
            processed = message

        elif self._mode is Mode.ENCRYPTED:
            # Placeholder "encryption": reverse string
            processed = message[::-1]

        elif self._mode is Mode.COMPRESSED:
            # Placeholder "compression": remove vowels
            processed = "".join(ch for ch in message if ch.lower() not in "aeiou")

        else:
            raise ValueError(f"Unknown mode: {self._mode}")

        print(f"[SEND] mode={self._mode.value} payload={processed}")
        return processed


def main() -> None:
    client = ChatClient()

    client.send("Hello World")

    client.set_mode(Mode.ENCRYPTED)
    client.send("Hello World")

    client.set_mode(Mode.COMPRESSED)
    client.send("Hello World")


if __name__ == "__main__":
    main()
