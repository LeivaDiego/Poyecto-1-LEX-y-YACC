# Importa la libreria encargada de dibujar el grafo
from graphviz import Digraph


# Definicion de los nodos del grafo dirigido
# Clase que representa un nodo del arbol 
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Generador del grafo dirigido de la expresion--------------------------------------------

# Para manejar la expresion <=> 
def format_label(value):
    # Si el valor es <=>, devolverlo encerrado en comillas
    if value == '<=>':
        return '\<=>'
    # En caso contrario, devolver el valor tal cual
    return value


# Esta funcion es la que toma el arbol y genera un grafo dirigido usando Graphviz 
# (Herramienta vista en teoria de la computacion)
def plot_tree(root, graph=None):
    
    # Si no se da un grafo existente, se inicializa uno nuevo
    if graph is None:
        graph = Digraph()
        # Se crea un nodo en el grafo para el nodo raiz del arbol
        graph.node(name=str(id(root)), label=format_label(root.value))
    
    # Si el nodo actual tiene un hijo izquierdo, se agrega al grafo
    if root.left:
        # Se crea un nodo para el hijo izquierdo
        graph.node(name=str(id(root.left)), label=format_label(root.left.value))
        # Se crea una arista entre el nodo actual y su hijo izquierdo
        graph.edge(str(id(root)), str(id(root.left)))
        # Llamada recursiva para seguir construyendo el grafo con el hijo izquierdo
        plot_tree(root.left, graph)
    
    # Si el nodo actual tiene un hijo derecho, se agrega al grafo
    if root.right:
        # Se crea un nodo para el hijo derecho
        graph.node(name=str(id(root.right)),label=format_label(root.right.value))
        # Se crea una arista entre el nodo actual y su hijo derecho
        graph.edge(str(id(root)), str(id(root.right)))
        # Llamada recursiva para seguir construyendo el grafo con el hijo derecho
        plot_tree(root.right, graph)
    
    # Devuelve el grafo construido
    return graph
