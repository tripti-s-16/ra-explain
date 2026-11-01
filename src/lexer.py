import re

TOKEN_SPEC = [
    ('SELECT', r'SELECT\b'), ('FROM', r'FROM\b'), ('WHERE', r'WHERE\b'),
    ('JOIN', r'JOIN\b'), ('ON', r'ON\b'), ('AND', r'AND\b'), ('OR', r'OR\b'),
    ('COMMA', r','), ('EQ', r'='), ('GT', r'>'), ('LT', r'<'),
    ('NUMBER', r'\d+'), ('STRING', r"'[^']*'"),
    ('IDENT', r'[a-zA-Z_][a-zA-Z0-9_.]*'), ('SKIP', r'\s+'), ('MISMATCH', r'.')
]

def tokenize(sql):
    tokens = []
    pattern = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)
    for mo in re.finditer(pattern, sql, re.IGNORECASE):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        if kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r}')
        tokens.append((kind.upper(), value))
    return tokens
