from lexer import Lexer

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
        ('MUL', '\+'),
        ('DIV', '\+'),
        ('LPAREN', '('),
        ('RPAREN', ')'),
    ]
    lexer.set_rules(rules)
    tokens = lexer.get_tokens(get_file_text('simple.sc'))
    print(tokens)

if __name__ == '__main__':
    run()