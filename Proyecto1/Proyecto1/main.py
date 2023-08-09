from parser_module import lexer, parser, plot_tree



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

for index, expr in enumerate(expressions):
    lexer.input(expr)
    resultado = parser.parse(expr)
    tree_graph = plot_tree(resultado)
    tree_graph.view(filename=f"syntax_tree{index}.gv")

    





