import _ast
import ast

import networkx as nx


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.stack = []
        self.graph = nx.DiGraph()
        self.labels = {}

    def generic_visit(self, node):
        node_name = f'({node})'

        node_label = node.__class__.__name__
        if hasattr(node, 'id'):
            node_label = f'\"{node.id}\"'
        if node_label == 'Load':
            return
        self.labels[node_name] = node_label

        parent_name = None
        if self.stack:
            parent_name = self.stack[-1]

        self.stack.append(node_name)
        self.graph.add_node(node_name)

        if parent_name:
            self.graph.add_edge(parent_name, node_name)

        super().generic_visit(node)
        self.stack.pop()
