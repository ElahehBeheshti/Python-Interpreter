import re

# Token specification
TOKEN_SPEC = [
    ("LET", r"let"),       # Keyword 'let'
    ("PRINT", r"print"),   # Keyword 'print'
    ("ID", r"[a-zA-Z_][a-zA-Z_0-9]*"),  # General identifier
    ("NUMBER", r"\d+"),
    ("ASSIGN", r"="),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MUL", r"\*"),
    ("DIV", r"/"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("SEMI", r";"),
    ("SKIP", r"[ \t]+"),   # Skip spaces and tabs
    ("MISMATCH", r"."),    # Any other character
]

# Tokenizer function
def tokenize(code):
    token_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in TOKEN_SPEC)
    line_num = 1
    line_start = 0
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        column = match.start() - line_start
        if kind == "NUMBER":
            value = int(value)
        elif kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            raise SyntaxError(f"Unexpected character {value} at line {line_num}, column {column}")
        yield (kind, value)








