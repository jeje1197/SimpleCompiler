import re

class Token:
    def __init__(self, type, value, start_pos, end_pos):
        self.type = type
        self.value = value
        self.start_pos = start_pos
        self.end_pos = end_pos

    def __repr__(self) -> str:
        return f"({self.type})"

class Position:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.idx = 0
        self.ln = 1
        self.col = 1
    
    def advance(self, cur_char):
        if cur_char == '\n':
            self.ln += 1
            self.col = 1
        else:
            self.col += 1
        self.idx += 1

    def copy(self):
        pos = Position(self.fn, self.text)
        pos.idx = self.idx
        pos.ln = self.ln
        pos.col = self.col
        return pos

    def __repr__(self):
        return f'ln: {self.ln}, col: {self.col}'

class Lexer:
    def __init__(self):
        self.rules = None # (token_type, regex)

    def set_rules(self, rules:list):
        if len(rules) == 0:
            raise Exception(f"No rules were passed in: {rules}")

        for rule in rules:
            if not (isinstance(rule[0], str) or isinstance(rule[1], str)):
                raise Exception(f"Expected rule of format '(token_type, regex)', but got '{rule}'")
        self.rules = rules
            
    def get_tokens(self, text):
        tokens = []
        pos = Position('Lexer', text)

        while len(text) > 0:
            rule_matched = False
            for rule in self.rules:
                match = re.match(rule[1], text)

                if match:
                    value = match.group(0)

                    pos_start = pos.copy()
                    for char in value:
                        pos.advance(char)
                    pos_end = pos.copy()
                    
                    if not rule[0] in ('skip', 'SKIP'):
                        tokens.append(Token(rule[0], value, pos_start, pos_end))
                    text = text[len(value):]
                    rule_matched = True
                    break
            
            if not rule_matched:
                raise Exception(f"No rule found for '{text}'. \nPosition: {pos}")
        
        return tokens


# Example
if __name__ == '__main__':
    lexer = Lexer()
    rules = [
        ('SKIP', '//.*\n?'),
        ('SKIP', ' '),
        ('NEWLINE', '\n'),
        ('NUMBER', '[0-9]+(\.[0-9]+)?'),
        ('PLUS', '\+'),
        ('ID', '[a-zA-Z_][a-zA-Z_0-9]*')
    ]

    lexer.set_rules(rules)
    tokens = lexer.get_tokens("12.2+2+4 \n hi")
    print(tokens)

