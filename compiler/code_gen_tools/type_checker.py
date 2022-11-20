from .classes import Number, String

class TypeChecker:
    def __init__(self) -> None:
        pass

    def visit(self, node):
        node_type = type(node).__name__
        method = getattr(self, f'visit_{node_type}', self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f"No visit method for {type(node).__name__}")

    def visit_list(self, node):
        for element in node:
            self.visit(element)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_StringNode(self, node):
        return String(node.value)

    def visit_BinOpNode(self, node):
        left = self.visit(node.left_node)
        right = self.visit(node.right_node)

        if type(left).__name__ != type(right).__name__:
            raise Exception(f"Operation: '{node.op.value}' cannot be performed on {type(left)} and {type(right)}")

        if isinstance(left, String):
            if node.op.type != 'PLUS':
                raise Exception(f"Invalid operator for string: '{node.op.value}'")
        return left

    def visit_Command(self, node):
        cmd_list = ["print"]
        cmd_name = node.name
        if cmd_name not in cmd_list:
            raise Exception(f"Command not defined: '{cmd_name}'")
        self.visit(node.expr)
