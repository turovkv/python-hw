import ast
import inspect

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

from ast_visitor import Visitor
from fibonacci import get_fib_list


def print_ast():
    ast_object = ast.parse(inspect.getsource(get_fib_list))
    v = Visitor()
    v.visit(ast_object)
    plt.figure(1, (15, 10))
    nx.draw(
        G=v.graph,
        pos=graphviz_layout(v.graph, prog="dot"),
        with_labels=True,
        labels=v.labels,
        node_shape='o',
        node_size=v.sizes,
        node_color=v.colors,
        font_size=8)
    plt.savefig("artifacts/graph.png")


if __name__ == "__main__":
    print_ast()
