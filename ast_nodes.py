class ASTNode:
    pass

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class AssignNode(ASTNode):
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class VarNode(ASTNode):
    def __init__(self, name):
        self.name = name

class NumNode(ASTNode):
    def __init__(self, value):
        self.value = value