# ra-explain

A minimal SQL → Relational Algebra compiler.

## What it does
Converts `SELECT ... FROM ... WHERE ... JOIN ...` into RA expressions like `π_name(σ_age>20(students))` and applies selection pushdown optimization.

## Why
Core component of DBMS query processing (COL362). Demonstrates parsing, AST generation, and logical optimization.

## Run
```bash
python main.py --sql "SELECT name FROM students WHERE age > 20"
