# Importa la libreria lex
from ply import lex


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

# Construccion del analizador lexico
lexer = lex.lex()
