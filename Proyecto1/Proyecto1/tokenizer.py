from .ply import lex

# Definici�n de los tokens (s�mbolos l�xicos)
tokens = [
    'VAR',              # Variables proposicionales
    'NOT',              # Operador de negaci�n (~)
    'AND',              # Operador de conjunci�n (^)
    'OR',               # Operador de disjunci�n (o)
    'IMPLIES',          # Operador de implicaci�n (=>)
    'EQUIVALENCE',      # Operador de equivalencia (<=>)
    'LPAREN',           # Par�ntesis izquierdo
    'RPAREN',           # Par�ntesis derecho
    'TRUE',             # Constante 0 para valor de verdad falso
    'FALSE',            # Constante 1 para valor de verdad verdadero
]

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
    print(f"Caracter no v�lido: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()