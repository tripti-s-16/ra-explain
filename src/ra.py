def to_ra(ast):
    table = ast['table']
    where = ast['where']
    joins = ast['joins']
    cols = ast['columns']
    
    expr = table
    
    for jtable, left, right in joins:
        expr = f"({expr} ⋈_{left}={right} {jtable})"
    
    if where:
        expr = f"σ_{where}({expr})"
    
    if cols and cols != ['*']:
        col_str = ",".join(cols)
        expr = f"π_{col_str}({expr})"
    
    return expr

def explain_steps(ast):
    steps = []
    steps.append(f"1. Start with table: {ast['table']}")
    if ast['joins']:
        for jtable, left, right in ast['joins']:
            steps.append(f"2. JOIN with {jtable} ON {left}={right}")
    if ast['where']:
        steps.append(f"3. Apply selection: σ_{ast['where']}")
    if ast['columns']:
        steps.append(f"4. Project columns: {ast['columns']}")
    return "\n".join(steps)
