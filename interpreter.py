from ast_nodes import *

class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, statements):
        for stmt in statements:
            self.execute(stmt)

    def execute(self, node):
        if isinstance(node, AssignNode):
            value = self.evaluate(node.expr)
            self.variables[node.var] = value
        elif isinstance(node, PrintNode):
            value = self.evaluate(node.expr)
            print(value)
        else:
            raise TypeError(f"Unknown node type {type(node)}")

    def evaluate(self, node):
        if isinstance(node, NumNode):
            return node.value
        elif isinstance(node, VarNode):
            if node.name in self.variables:
                return self.variables[node.name]
            else:
                raise NameError(f"Undefined variable {node.name}")
        elif isinstance(node, BinOpNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            if node.op == "+":
                return left + right
            elif node.op == "-":
                return left - right
            elif node.op == "*":
                return left * right
            elif node.op == "/":
                return left / right
            else:
                raise TypeError(f"Unknown operator {node.op}")
        else:
            raise TypeError(f"Unknown node type {type(node)}")