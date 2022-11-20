from .classes import Number, String, BinOp

INITIALIZER_CODE = """\
#include <stdio.h>
#include <string.h>

char* addStrings(char* str1, char* str2, char* dest) {
    strcat(dest, str1);
	strcat(dest, str2);
    return dest;
}

/* Compiled from SimpleC to C */
"""

MAIN_START = """\
int main(int argc, char *argv[]) {
	char dest[80] = "";
"""

MAIN_END = """\
    return 0;
}"""

class CodeGenerator:
    def __init__(self) -> None:
        self.output = ""

    def generate_code(self, ast, file_name) -> None:
        self.visit(ast)

        generated_code = INITIALIZER_CODE + MAIN_START + self.output + MAIN_END
        
        # Write to file
        f = open(file_name, 'w')
        f.write(generated_code)
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

        if isinstance(left, String):
            return String(f'addStrings({left}, {right}, dest)')
        elif isinstance(left, Number):
            return Number(f'({left} {op} {right})')

    def visit_Command(self, node):
        cmd_name = node.name
        arg = self.visit(node.expr)

        if isinstance(arg, BinOp):
            if arg.type == 'Number':
                arg = Number(arg.value)
            elif arg.type == 'String':
                arg = String(arg.value)
            else: 
                raise Exception("BinOp not changed")

        if cmd_name == 'print':
            print_statement = '\tprintf("'
            if isinstance(arg, Number):
                print_statement += '%d'
            elif isinstance(arg, String):
                print_statement += '%s'
            else:
                raise Exception("Error: Print statement")
            print_statement += f'\\n", {arg.value});\n'

            self.output += print_statement
