import ast

import networkx as nx

color = {
    1: "tab:red",
    2: "tab:orange",
    3: "tab:olive",
    4: "tab:green",
    5: "tab:blue",
    6: "tab:purple",
}


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.stack = []
        self.graph = nx.DiGraph()
        self.labels = {}
        self.node_counts = {}
        self.colors = []
        self.sizes = []

    def get_node_color(self, node):
        color = "tab:olive"
        if node.__class__.__name__ == 'Constant':
            color = "tab:orange"
        if node.__class__.__name__ == 'Call':
            color = "tab:purple"
        if node.__class__.__name__ == 'Name':
            color = "tab:green"
        if node.__class__.__name__ == 'Load':
            color = "tab:blue"
        return color

    def get_node_name(self, node):
        node_name = f'({node})'
        cnt = 1
        if node_name in self.node_counts:
            cnt = self.node_counts[node_name] + 1
        self.node_counts[node_name] = cnt
        node_name = f'{node_name}{cnt}'
        return node_name

    def get_node_label(self, node):
        node_label = node.__class__.__name__
        if hasattr(node, 'id'):
            node_label = f'{node_label}\n\"{node.id}\"'
        if node_label == 'Constant':
            node_label = f'{node_label}\n{node.value}'
        if node_label == 'arg':
            node_label = f'{node_label}\n{node.arg}'
        if node_label == 'FunctionDef':
            node_label = f'{node_label}\n{node.name}'
        return node_label

    def generic_visit(self, node):
        node_name = self.get_node_name(node)
        node_label = self.get_node_label(node)
        self.labels[node_name] = node_label
        self.colors.append(self.get_node_color(node))
        self.sizes.append(160 * (3 + len(node_label)))
        parent_name = None
        if self.stack:
            parent_name = self.stack[-1]

        self.stack.append(node_name)
        self.graph.add_node(node_name)

        if parent_name:
            self.graph.add_edge(parent_name, node_name)

        super().generic_visit(node)
        self.stack.pop()
