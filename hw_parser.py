from parser_classes import Command, StringNode, NumberNode, BinOp

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.next = tokens[0]

    def get_next(self):
        if self.index + 1 < len(self.tokens):
            self.index += 1
            self.next = self.tokens[self.index]
        else:
            self.next = None

    def parse(self):
        return self.statement()

    def statement(self):
        if not self.next.type == 'ID':
            raise Exception("Invalid Statement" + str(self.next.start_pos))
        command_name = self.next.value
        self.get_next()

        expr_node = self.expr()
        if not expr_node:
            raise Exception("Invalid expression after command")

        return Command(command_name, expr_node)

    def expr(self):
        return self.bin_op(self.term, ("PLUS", "MINUS"), self.term)

    def term(self):
        return self.bin_op(self.factor, ("MUL", "DIV"), self.factor)

    def factor(self):
        token = self.next
        if token.type == 'NUMBER':
            self.get_next()
            return NumberNode(token.value)
        elif token.type == 'STRING':
            self.get_next()
            return StringNode(token.value)
        elif token.type == 'LPAREN':
            self.get_next()
            expr_node = self.expr()
            if not self.next.type == 'RPAREN':
                raise Exception("Unbalanced Parentheses")
            self.get_next()
            return expr_node
        return None

    def bin_op(self, function1, ops, function2):
        left = function1()

        while self.next and self.next.type in ops:
            op = self.next
            self.get_next()
            left = BinOp(left, op, function2())
        return left
    