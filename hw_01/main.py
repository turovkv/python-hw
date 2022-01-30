import ast
import inspect

import astunparse
import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

from fibonacci import get_fib_list
from graph_builder import Visitor


def print_ast():
    ast_object = ast.parse(inspect.getsource(get_fib_list))
    v = Visitor()
    v.visit(ast_object)
    nx.draw(v.graph, pos=graphviz_layout(v.graph, prog="dot"), with_labels=True, labels=v.labels, font_size=8)
    plt.savefig("artifacts/graph.png")


if __name__ == "__main__":
    print_ast()
