from .classes import Number, String, BinOp

class CodeGenerator:
    def __init__(self) -> None:
        self.output = ""

    def generate_code(self, ast, file_name) -> None:
        init_code = '#include <stdio.h>\n\n'
        init_code += '// Compiled from Simple C to C\n'
        init_code += 'int main(int argc, char *argv[]) {\n'
        end_code = '\treturn 0;\n}'

        self.visit(ast)
        
        # Write to file
        f = open(file_name, 'w')
        f.write(init_code + self.output + end_code)
        print(f"File generated: '{file_name}'")

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

    def visit_BinOpNode(self, node) -> str:
        left = self.visit(node.left_node)
        op = node.op.value
        right = self.visit(node.right_node)
        return BinOp(type(left).__name__, f'({left} {op} {right})')

    def visit_Command(self, node):
        cmd_name = node.name
        arg = self.visit(node.expr)

        if isinstance(arg, BinOp):
            if arg.type == 'Number':
                arg = Number(arg.value)
            elif arg.type == 'String':
                arg = String(arg.value)

        if cmd_name == 'print':
            print_statement = '\tprintf("'
            if isinstance(arg, Number):
                print_statement += '%d'
            elif isinstance(arg, String):
                print_statement += '%s'
            else:
                raise Exception("Error: Print statement")
            print_statement += f'\\n", {arg});\n'

            self.output += print_statement
