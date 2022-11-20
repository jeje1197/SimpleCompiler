class Command:
    def __init__(self, name, expr) -> None:
        self.name = name
        self.expr = expr

    def __repr__(self) -> str:
        return f'{self.name} {self.expr}'

class StringNode:
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return self.value

class NumberNode:
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return self.value

class BinOpNode:
    def __init__(self, left_node, op, right_node) -> None:
        self.left_node = left_node
        self.op = op
        self.right_node = right_node

    def __repr__(self) -> str:
        return f'({self.left_node} {self.op} {self.right_node})'