from .lexer import tokenize

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def consume(self, expected=None):
        tok = self.peek()
        if expected and tok[0] != expected:
            raise SyntaxError(f"Expected {expected} got {tok}")
        self.pos += 1
        return tok

    def parse(self):
        self.consume('SELECT')
        cols = []
        while True:
            kind, val = self.peek()
            if kind == 'IDENT':
                cols.append(self.consume()[1])
                if self.peek()[0] == 'COMMA':
                    self.consume('COMMA')
                else:
                    break
            else:
                break
        self.consume('FROM')
        table = self.consume('IDENT')[1]
        where = None
        joins = []
        if self.peek()[0] == 'WHERE':
            self.consume('WHERE')
            where = self.parse_condition()
        while self.peek()[0] == 'JOIN':
            self.consume('JOIN')
            jtable = self.consume('IDENT')[1]
            self.consume('ON')
            left = self.consume('IDENT')[1]
            self.consume('EQ')
            right = self.consume('IDENT')[1]
            joins.append((jtable, left, right))
        return {'columns': cols, 'table': table, 'where': where, 'joins': joins}

    def parse_condition(self):
        left = self.consume('IDENT')[1]
        op_tok = self.consume()
        op = op_tok[1]
        right = self.consume()[1]
        cond = f"{left}{op}{right}"
        if self.peek()[0] == 'AND':
            self.consume('AND')
            cond += " AND " + self.parse_condition()
        return cond

def parse_sql(sql):
    tokens = tokenize(sql)
    p = Parser(tokens)
    return p.parse()
