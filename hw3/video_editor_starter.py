class VideoEditor:
    def __init__(self) -> None:
        self._contrast = 0.5
        self._text = ""

    def set_text(self, text: str) -> None:
        self._text = text

    def remove_text(self) -> None:
        self._text = ""

    def get_contrast(self) -> float:
        return self._contrast

    def set_contrast(self, contrast: float) -> None:
        self._contrast = contrast

    def __str__(self) -> str:
        return f"VideoEditor(contrast={self._contrast}, text={self._text!r})"
