class NT:
    def __init__(self) -> None:
        self.list = []

    def add_production(self, production:list):
        if not production:
            raise Exception("Production not defined")
        self.list.append(production)

    def match(self):
        pass

    def return_function(data):
        return data

class Term:
    def __init__(self, token_type, token_value=None) -> None:
        self.type = token_type
        self.value = token_value
        self.match_value = True if token_value else False

    def match(self, token):
        if self.match_value:
            return token.value == self.value
        else:
            return token.type == self.type and token.value == self.value

class Parser:
    def __init__(self) -> None:
        self.entry_rule = None

    def set_entry_rule(self, entry_rule):
        if not isinstance(entry_rule, NT):

    


