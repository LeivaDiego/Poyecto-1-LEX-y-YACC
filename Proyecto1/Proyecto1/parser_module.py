# Importacion de librerias necesarias
from ply import lex
from ply import yacc
from graphviz import Digraph


# Definicion de los tokens (simbolos lexicos)---------------------------------------------

# Se definen los simbolos lexicos que el lexer reconocera
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
# cada linea de "t_nombre del token" define una expresion regular que representa como 
# se reconocera el token en el string de entrada
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
# Esto define la precedencia de simbolos en caso existan expresiones ambiguas
precedence = (
    ('left', 'IMPLICATION', 'BICONDITIONAL'),
    ('left', 'DISJUNCTION'),
    ('left', 'CONJUNCTION'),
    ('left', 'NEGATION')
)

# Construccion del analizador lexico
lexer = lex.lex()




# Definicion de los nodos del grafo dirigido
# Clase que representa un nodo del arbol 
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



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


# Generador del grafo dirigido de la expresion--------------------------------------------

# Esta funcion es la que toma el arbol y genera un grafo dirigido usando Graphviz 
# (Herramienta vista en teoria de la computacion)
def plot_tree(root, graph=None):
    
    # Si no se da un grafo existente, se inicializa uno nuevo
    if graph is None:
        graph = Digraph()
        # Se crea un nodo en el grafo para el nodo raiz del arbol
        graph.node(name=str(id(root)), label=root.value)
    
    # Si el nodo actual tiene un hijo izquierdo, se añade al grafo
    if root.left:
        # Se crea un nodo para el hijo izquierdo
        graph.node(name=str(id(root.left)), label=root.left.value)
        # Se crea una arista entre el nodo actual y su hijo izquierdo
        graph.edge(str(id(root)), str(id(root.left)))
        # Llamada recursiva para seguir construyendo el grafo con el hijo izquierdo
        plot_tree(root.left, graph)
    
    # Si el nodo actual tiene un hijo derecho, se añade al grafo
    if root.right:
        # Se crea un nodo para el hijo derecho
        graph.node(name=str(id(root.right)), label=root.right.value)
        # Se crea una arista entre el nodo actual y su hijo derecho
        graph.edge(str(id(root)), str(id(root.right)))
        # Llamada recursiva para seguir construyendo el grafo con el hijo derecho
        plot_tree(root.right, graph)
    
    # Devuelve el grafo construido
    return graph
