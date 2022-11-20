from parsing_tools.lexer import Lexer
from parsing_tools.hw_parser import Parser
from code_gen_tools.type_checker import TypeChecker

def get_file_text(file_name):
    f = open(file_name, 'r')
    file_text = f.read()
    f.close()
    return file_text

def run():
    lexer = Lexer()
    rules = [
        ('SKIP', '//.*\n?'), # Comments
        ('SKIP', ' |\t'), # White space
        ('NEWLINE', '\n'), # Newline
        ('NUMBER', '[0-9]+(\.[0-9]+)?'),
        ('STRING', '".*"'),
        ('ID', '[a-zA-Z_][a-zA-Z_0-9]*'),
        ('PLUS', '\+'),
        ('MINUS', '\+'),
        ('MUL', '\\'),
        ('DIV', '/'),
        ('LPAREN', '('),
        ('RPAREN', ')'),
    ]
    lexer.set_rules(rules)
    tokens = lexer.get_tokens(get_file_text('simple.sc'))

    parser = Parser(tokens)
    ast = parser.parse()
    # print(ast)

    tc = TypeChecker()
    tc.visit(ast)

    cg = CodeGenerator()
    cg.generate(ast)

if __name__ == '__main__':
    run()