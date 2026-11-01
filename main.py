import argparse
from src.parser import parse_sql
from src.ra import to_ra, explain_steps
from src.optimizer import optimize

def run(sql):
    print(f"\nInput SQL: {sql}\n")
    ast = parse_sql(sql)
    print(f"AST: {ast}\n")
    
    print("--- Steps ---")
    print(explain_steps(ast))
    
    optimized_ast, opt_explain = optimize(ast)
    print(f"\n--- Optimization ---")
    print(opt_explain)
    
    ra = to_ra(optimized_ast)
    print(f"\nFinal RA Expression:\n{ra}\n")
    return ra

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SQL to RA compiler")
    parser.add_argument('--sql', type=str, help='SQL query', default="SELECT name FROM students WHERE age > 20")
    args = parser.parse_args()
    run(args.sql)
