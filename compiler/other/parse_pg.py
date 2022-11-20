from lexer import Lexer

if __name__ == '__main__':
    lexer = Lexer()
    rules = [
        ('SKIP', '//.*\n?'), # Comments
        ('SKIP', '\s'), # White space
        ('STRING', '".*"'),
        ('RULEREF', '[a-zA-Z_][a-zA-Z_0-9]*'),
        ('PLUS', '\+'),
        ('KLEENE', '\*'),
        ('LPAREN', '\('),
        ('RPAREN', '\)'),
        ('OR', '\|')
    ]
    lexer.set_rules(rules)
    tokens = lexer.get_tokens("factor ((<PLUS>|<MINUS>) factor)*")
    print(tokens)