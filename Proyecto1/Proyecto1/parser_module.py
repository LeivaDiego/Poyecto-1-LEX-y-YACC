from ply import lex
from ply import yacc
from graphviz import Digraph


# Definicion de los tokens (simbolos lexicos)---------------------------------------------
tokens = (
    'VARIABLE',         # Variables proposicionales
    'NEGATION',         # Operador de negacion (~)
    'CONJUNCTION',      # Operador de conjuncion (^)
    'DISJUNCTION',      # Operador de disjuncion (o)
    'IMPLICATION',      # Operador de implicacion (=>)
    'BICONDITIONAL',    # Operador de equivalencia (<=>)
    'LPAREN',           # Parentesis izquierdo
    'RPAREN',           # Parentesis derecho
    'CONSTANT',         # Constante 0 o 1 para valor de verdad verdadero
    )


# Expresiones regulares para los tokens
t_NEGATION = r'\~'
t_CONJUNCTION = r'\^'
t_DISJUNCTION = r'o'
t_IMPLICATION = r'=>'
t_BICONDITIONAL = r'<=>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_VARIABLE = r'[p-z]'   
t_CONSTANT = r'[01]'

# Ignorar saltos de linea
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    
# Manejo de errores lexicos
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Precedencia de simbolos
precedence = (
    ('left', 'IMPLICATION', 'BICONDITIONAL'),
    ('left', 'DISJUNCTION'),
    ('left', 'CONJUNCTION'),
    ('left', 'NEGATION')
)

# Construccion del analizador lexico
lexer = lex.lex()




# Definicion de los nodos del grafo dirigido
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



# Reglas de la gramatica------------------------------------------------------------------

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


# Generador del grafo dirigido de la expresion--------------------------------------------

def plot_tree(root, graph=None):
    if graph is None:
        graph = Digraph()
        graph.node(name=str(id(root)), label=root.value)
    if root.left:
        graph.node(name=str(id(root.left)), label=root.left.value)
        graph.edge(str(id(root)), str(id(root.left)))
        plot_tree(root.left, graph)
    if root.right:
        graph.node(name=str(id(root.right)), label=root.right.value)
        graph.edge(str(id(root)), str(id(root.right)))
        plot_tree(root.right, graph)
    return graph