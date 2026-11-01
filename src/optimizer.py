def pushdown_selection(ast):
    """
    Selection pushdown: if WHERE condition is on base table,
    push it before JOIN. Classic optimization from database textbooks.
    """
    where = ast.get('where')
    if not where or not ast['joins']:
        return ast, False
    
    # Simple heuristic: if where clause contains only base table columns
    # (no join table columns), it can be pushed
    base_table = ast['table']
    can_push = base_table.split('.')[-1].lower() in where.lower() or '.' not in where
    
    if can_push:
        optimized = ast.copy()
        optimized['pushed'] = True
        return optimized, True
    return ast, False

def optimize(ast):
    new_ast, pushed = pushdown_selection(ast)
    explanation = ""
    if pushed:
        explanation = f"Optimization: Pushed σ_{ast['where']} before JOIN to reduce intermediate rows"
    else:
        explanation = "No pushdown applicable"
    return new_ast, explanation
