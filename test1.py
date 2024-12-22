from lexer import tokenize
from parser import Parser
from interpreter import Interpreter

# Sample code for the interpreter
code = """
let x = 10 + 5;
let y = x * 2;
print(x);
print(y);
"""

# Tokenize the input
tokens = list(tokenize(code))
print("Tokens:", tokens)

# Parse the tokens into an AST
parser = Parser(tokens)
ast = parser.parse()
print("\nAST:", ast)

# Interpret and execute the AST
interpreter = Interpreter()
print("\nExecution Output:")
interpreter.interpret(ast)