"""
Advent of Code 2020 - Utilities Module
https://adventofcode.com/2020/

PEP 8 compliant
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


class Graph():

    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes if nodes else set()
        self.edges = edges if edges else {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, nodeA, nodeB, cost=1, two_ways=False):
        self.nodes.add(nodeA)
        self.nodes.add(nodeB)
        self.edges[(nodeA, nodeB)] = cost
        if two_ways:
            self.edges[(nodeB, nodeA)] = cost

    def remove_node(self, node):
        self.nodes.remove(node)
        edges = (x for x in self.edges if (x[0] == node or x[1] == node))
        for edge in edges:
            del self.edges[edge]

    def _find_all_instream(self, node, upstream):
        open_set = set([node])
        closed_set = set()
        while open_set:
            node = open_set.pop()
            if upstream:
                add_nodes = [a for a, b in self.edges if b == node]
            else:
                add_nodes = [b for a, b in self.edges if a == node]
            closed_set.update(add_nodes)
            open_set.update(add_nodes)
        return closed_set

    def find_all_downstream(self, node):
        return self._find_all_instream(node, upstream=False)

    def find_all_upstream(self, node):
        return self._find_all_instream(node, upstream=True)
