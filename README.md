# Academic Prpject

# Python Interpreter Project (Advanced Programming Language Class)

## Introduction
This project involved creating a simple Python interpreter to execute a custom programming language. The interpreter processes variable assignments, arithmetic operations, and print statements sequentially, using a semicolon (`;`) as the statement separator.

-----------

## Project Structure
The project is divided into four key components:

### 1. Lexer (Ashok Chennareddy)
The **Lexer** is responsible for tokenizing raw input into meaningful symbols such as `NUMBER`, `ID`, `PLUS`, and `SEMI`.

#### Example:
Input: 
```plaintext
let x = 10 + 5;

Tokens produced:

[('LET', 'let'), ('ID', 'x'), ('ASSIGN', '='), ('NUMBER', 10), 
('PLUS', '+'), ('NUMBER', 5), ('SEMI', ';')]

-----------

### 2. Parser (Sri Pavan Kalyan Reddy Gottam)
The Parser takes these tokens and constructs an Abstract Syntax Tree (AST), representing the logical structure of the program.

Example:

Input:
let x = 10 + 5;

AST produced:
AssignNode(var='x', expr=BinOpNode(left=NumNode(10), op='+', right=NumNode(5)))

-----------

3. AST Nodes (Sai Prashanth Reddy Dyapa)
The AST Nodes define the fundamental constructs of the programming language. These include:

NumNode: Represents numeric values.
VarNode: Represents variables.
BinOpNode: Represents arithmetic operations.
AssignNode: Represents variable assignments.
PrintNode: Represents print statements.

-----------

4. Interpreter (Elaheh Beheshti)
The Interpreter traverses the AST and executes its nodes. Key functionalities include:

Arithmetic Evaluation: Recursively evaluates arithmetic expressions.
Variable Assignment: Maintains variable states in a dictionary (self.variables).
Expression Output: Prints the results of evaluated expressions.

-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------


Example Programs

Test 1
Input:
let x = 10 + 5;
let y = x * 2;
print(x);
print(y);

BNF Mapping:
<program> ::= 
    "let" <identifier> "=" <number> ";"
    "let" <identifier> "=" <identifier> "*" <number> ";"
    "print" "(" <identifier> ")" ";"
    "print" "(" <identifier> ")" ";"

Output:

15
30

-----------------------------------------------

Test 2
Input:
let a = 2;
let b = a * 5;
let c = b - 3;
print(c);

BNF Mapping:
<program> ::= 
    "let" <identifier> "=" <number> ";"
    "let" <identifier> "=" <identifier> "*" <number> ";"
    "let" <identifier> "=" <identifier> "-" <number> ";"
    "print" "(" <identifier> ")" ";"

Output:
7
-----------------------------------------------
Test 3
Input:
let p = 8;
let q = 16 / 2;
print(p);
print(q);

BNF Mapping:
<program> ::= 
    "let" <identifier> "=" <number> ";"
    "let" <identifier> "=" <number> "/" <number> ";"
    "print" "(" <identifier> ")" ";"
    "print" "(" <identifier> ")" ";"


Output:
8
8