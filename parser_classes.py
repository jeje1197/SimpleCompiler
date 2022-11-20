class Command:
    def __init__(self, name, expr) -> None:
        self.name = name
        self.expr = expr

class StringNode:
    def __init__(self, value) -> None:
        self.value = value

class NumberNode:
    def __init__(self, value) -> None:
        self.value = value

class BinOp:
    def __init__(self, left_node, op, right_node) -> None:
        self.left_node = left_node
        self.op = op
        self.right_node = right_node

    def __repr__(self) -> str:
        pass