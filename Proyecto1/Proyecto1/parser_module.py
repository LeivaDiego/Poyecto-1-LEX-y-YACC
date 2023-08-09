from ply import yacc
from ply import lex
from graphviz import Digraph


# Definicion de los tokens (símbolos lexicos)---------------------------------------------
tokens = (
    'VAR',              # Variables proposicionales
    'NOT',              # Operador de negacion (~)
    'AND',              # Operador de conjuncion (^)
    'OR',               # Operador de disjuncion (o)
    'IMPLIES',          # Operador de implicacion (=>)
    'EQUIVALENCE',      # Operador de equivalencia (<=>)
    'LPAREN',           # Parentesis izquierdo
    'RPAREN',           # Parentesis derecho
    'TRUE',             # Constante 0 para valor de verdad falso
    'FALSE',            # Constante 1 para valor de verdad verdadero
)

# Tokens
t_VAR = r'[p-z]'
t_NOT = r'~'
t_AND = r'\^'
t_OR = r'o'
t_IMPLIES = r'=>'
t_EQUIVALENCE = r'<=>'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_TRUE(t):
    r'1'
    t.value = True
    return t

def t_FALSE(t):
    r'0'
    t.value = False
    return t

t_ignore = " \t"

def t_error(t):
    print(f"Caracter no valido: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()



# Definiciones de la gramatica para el parser---------------------------------------------
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

parser = yacc.yacc()



# Generador del grafo dirigido de la expresion--------------------------------------------

def plot_ast(ast, index):
    dot = Digraph(comment=f'AST for formula {index}')

    def add_nodes(node, parent=None):
        if not node:
            return
        label = node[0]
        dot.node(str(node), label)
        if parent:
            dot.edge(str(parent), str(node))
        for child in node[1:]:
            add_nodes(child, node)

    add_nodes(ast)
    dot.view(filename=f"ast_graph_{index}.gv", cleanup=True)

def parse_and_plot(formula, index):
    result = parser.parse(formula, lexer=lexer)
    plot_ast(result, index)