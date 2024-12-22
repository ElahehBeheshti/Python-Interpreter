from lexer import tokenize
from parser import Parser
from interpreter import Interpreter

# Test programs as individual code snippets
program1 = """
let x = 10;
let y = x + 20;
print(y);
"""

program2 = """
let a = 2;
let b = a * 5;
let c = b - 3;
print(c);
"""

program3 = """
let p = 8;
let q = 16 / 2;
print(p);
print(q);
"""

def run_program(code, program_name):
    """Function to tokenize, parse, and interpret a program."""
    print(f"\nRunning {program_name}:\n{'-' * len(program_name)}")
    
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

# Running each program separately
if __name__ == "__main__":
    run_program(program1, "Program 1")
    run_program(program2, "Program 2")
    run_program(program3, "Program 3")
