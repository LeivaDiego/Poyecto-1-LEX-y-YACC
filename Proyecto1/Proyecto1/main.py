# Importacion del analizador lexico, el parser y el generador del grafo del modulo
from parser_module import parser
from lexer_module import lexer
from graph_module import plot_tree

# Declaracion de las expresiones a evaluar
expressions = [
    "p",
    "~~~q",
    "(p^q)",
    "(0=>(ros))",
    "~(p^q)",
    "(p<=>~p)",
    "((p=>q)^p)",
    "(~(p^(qor))os)"
]

# Ciclo que itera cada expresion, la analiza y genera su grafo respectivo
for index, expr in enumerate(expressions):
    lexer.input(expr)
    resultado = parser.parse(expr)
    tree_graph = plot_tree(resultado)
    tree_graph.view(filename=f"syntax_tree{index}.gv")