from ast_nodes import *
class Parser:
    
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.current_token = None
        self.next_token()

    def next_token(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def match(self, token_type):
        """Ensures the current token matches the expected type, then advances."""
        if self.current_token and self.current_token[0] == token_type:
            value = self.current_token[1]
            self.next_token()
            return value
        else:
            raise SyntaxError(f"Expected {token_type} but got {self.current_token}")

    def parse(self):
        """Parses the tokens and generates an Abstract Syntax Tree (AST)."""
        statements = []
        while self.current_token:
            if self.current_token[0] == "LET":
                statements.append(self.parse_assignment())
            elif self.current_token[0] == "PRINT":
                statements.append(self.parse_print())
            else:
                raise SyntaxError(f"Unexpected token {self.current_token}")
        return statements

    def parse_assignment(self):
        """Parses a variable assignment statement."""
        self.match("LET")
        var_name = self.match("ID")
        self.match("ASSIGN")
        expr = self.parse_expression()
        self.match("SEMI")
        return AssignNode(var_name, expr)

    def parse_print(self):
        """Parses a print statement."""
        self.match("PRINT")
        self.match("LPAREN")
        expr = self.parse_expression()
        self.match("RPAREN")
        self.match("SEMI")
        return PrintNode(expr)
    
    def parse_expression(self):
        left = self.parse_term()
        while self.current_token and self.current_token[0] in ("PLUS", "MINUS"):
            op = self.match(self.current_token[0])
            if op == "PLUS":
                op = "+"
            elif op == "MINUS":
                op = "-"
            right = self.parse_term()
            left = BinOpNode(left, op, right)
        return left
    
    def parse_term(self):
        left = self.parse_factor()
        while self.current_token and self.current_token[0] in ("MUL", "DIV"):
            op = self.match(self.current_token[0])
            if op == "MUL":
                op = "*"
            elif op == "DIV":
                op = "/"
            right = self.parse_factor()
            left = BinOpNode(left, op, right)
        return left
    
    def parse_factor(self):
        if self.current_token[0] == "NUMBER":
            return NumNode(self.match("NUMBER"))
        elif self.current_token[0] == "ID":
            return VarNode(self.match("ID"))
        elif self.current_token[0] == "LPAREN":
            self.match("LPAREN")
            expr = self.parse_expression()
            self.match("RPAREN")
            return expr
        else:
            raise SyntaxError(f"Unexpected token {self.current_token}")