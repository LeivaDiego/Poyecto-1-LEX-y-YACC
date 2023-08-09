import parser_module

formulas = [
    "p",
    "~~~q",
    "(p^q)",
    "(0=>(ros))",
    "~(p^q)",
    "(p<=>~p)",
    "((p=>q)^p)",
    "(~(p^(qor))os)"
]

parser_module.parse_and_plot(formulas[6], 6)
