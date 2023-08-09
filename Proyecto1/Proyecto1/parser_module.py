# Importacion de librerias necesarias
from ply import yacc

# Importa los tokens del modulo lexer
from lexer_module import tokens

# Importa la definicion de nodo
from graph_module import Node


# Precedencia de simbolos
# Esto define la precedencia de simbolos en caso existan expresiones ambiguas
precedence = (
    ('left', 'IMPLICATION', 'BICONDITIONAL'),
    ('left', 'DISJUNCTION'),
    ('left', 'CONJUNCTION'),
    ('left', 'NEGATION')
)


# Reglas de la gramatica------------------------------------------------------------------

# Estas funciones definen la estructura de la gramatica y como se construira el arbol 
# a partir de la entrada.

# Para las variables o constantes
def p_expression_value(p):
    '''
    expression : VARIABLE
                | CONSTANT
    '''
    p[0] = Node(p[1])

# Para las negaciones
def p_expression_negation(p):
    '''
    expression : NEGATION expression
    '''
    node = Node(p[1])
    node.right = p[2]
    p[0] = node

# Para los parentesis
def p_factor_grouped(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2]

# Para las expresiones con operadores logicos de AND, OR, IMPLIES, BICONDITIONAL
def p_expression(p):
    '''
    expression : expression CONJUNCTION expression
               | expression DISJUNCTION expression
               | expression IMPLICATION expression
               | expression BICONDITIONAL expression
    '''
    node = Node(p[2])
    node.left = p[1]
    node.right = p[3]
    p[0] = node

# Manejo de errores
def p_error(p):
    print(f'Syntax error at {p.value!r}')

# Construccion del Parser
parser = yacc.yacc()