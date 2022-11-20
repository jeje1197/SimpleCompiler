class Number:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

class String:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

class BinOp:
    def __init__(self, type, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value