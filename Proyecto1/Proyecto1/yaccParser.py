from .ply import yacc


def p_formula_var(p):
    '''formula : VAR
               | TRUE
               | FALSE'''
    p[0] = p[1]

def p_formula_not(p):
    'formula : NOT formula'
    p[0] = ('not', p[2])

def p_formula_binop(p):
    '''formula : formula AND formula
               | formula OR formula
               | formula IMPLIES formula
               | formula EQUIVALENCE formula'''
    p[0] = (p[2], p[1], p[3])

def p_formula_parens(p):
    'formula : LPAREN formula RPAREN'
    p[0] = p[2]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc()