"""
Advent of Code 2020 - Utilities Module
https://adventofcode.com/2020/

PEP 8 compliant
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


import re
from collections import namedtuple
from enum import Enum
from itertools import product


class Graph():
    """
    nodes is a dict {node_i: node_i_value}
    edges is a dict {node_i: {node_j: edge_ij_value}
    """

    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node, value=None):
        self.nodes[node] = value
        self.edges[node] = {}

    def add_edge(self, nodeA, nodeB, cost=1, two_ways=False):
        for node in (nodeA, nodeB):
            if node not in self.nodes:
                self.add_node(node)  # Default to a None-valued node
        self.edges[nodeA][nodeB] = cost
        if two_ways:
            self.edges[nodeB][nodeA] = cost

    def remove_node(self, node):
        del self.nodes[node]
        del self.edges[node]
        for edge in self.edges:
            edge.pop(node)  # Works also if node is not there

    def _find_all_instream(self, node, upstream):
        open_set = set([node])
        closed_set = set()
        while open_set:
            node = open_set.pop()
            if upstream:
                add_nodes = [source for source in self.edges
                             if node in self.edges[source]]
            else:
                add_nodes = self.edges[node].keys()
            closed_set.update(add_nodes)
            open_set.update(add_nodes)
        return closed_set

    def find_all_downstream(self, node):
        return self._find_all_instream(node, upstream=False)

    def find_all_upstream(self, node):
        return self._find_all_instream(node, upstream=True)


class Grid(Graph):

    Neighbourhood = Enum('Neighbourhood', 'MOORE VON_NEUMANN')

    def __init__(self, dimensions, values=lambda x: None,
                 neighbourhood=Neighbourhood.MOORE):
        """For each node, its value is set to values(node_coordinates)
        """
        super().__init__()
        for coordinate in product(*(range(d) for d in dimensions)):
            self.add_node(coordinate, values(coordinate))
        # Case #1: von Neumann neighbourhood
        if neighbourhood == self.Neighbourhood.VON_NEUMANN:
            variations = []
            for i in range(len(dimensions)):
                for step in (-1, +1):
                    variations.append(tuple(step*(i == j)
                                            for j in range(len(dimensions))))
        # Case #2: Moore neighbourhood
        elif neighbourhood == self.Neighbourhood.MOORE:
            variations = list(product((-1, 0, +1), repeat=len(dimensions)))
        # Case #N: Unrecognized neighbourhood
        else:
            raise ValueError(f"Unrecognized neighbourhood: {neighbourhood}")
        # Add edges to neighbours for each node
        for node in self.nodes:
            for variation in variations:
                neighbour = tuple(x + v for x, v in zip(node, variation))
                if all(0 <= x < d for x, d in zip(neighbour, dimensions)):
                    if neighbour != node:
                        self.add_edge(node, neighbour)

    @classmethod
    def from_nested_sequences(cls, main_sequence, depth,
                              values_map=lambda x: None,
                              neighbourhood=Neighbourhood.MOORE):
        """For each node, its value is set to values_map(sequences_value)
        """
        def values(coordinates):
            v = main_sequence
            for x in coordinates:
                v = v[x]
            return values_map(v)
        dimensions = []
        sub_sequence = main_sequence
        for _ in range(depth):
            dimensions.append(len(sub_sequence))
            sub_sequence = sub_sequence[0]
        return cls(tuple(dimensions), values, neighbourhood)


class Processor():
    # TODO: Possibly refactor this

    class IPOverflow(RuntimeError):
        pass

    class InfiniteLoop(RuntimeError):
        pass

    def __init__(self, memory=None):
        self.memory = memory if memory else []
        self.ip = 0
        self.acc = 0
        self.halted = False

    @classmethod
    def load_from_file(cls, file):
        with open(file) as ifile:
            # Obtain a list of [opcode, value] pairs in string form
            commands = [line.split() for line in ifile]
        return cls.load_from_cmd_list(commands)

    @classmethod
    def load_from_cmd_list(cls, commands):
        machine_code = [(cls.assembler(fun_str), int(value_str))
                        for fun_str, value_str in commands]
        machine_code.append((cls._hcf, 0))  # Program termination
        return cls(memory=machine_code)

    @classmethod
    def assembler(cls, key):
        # TODO: find a way to make this static and not dynamically generated
        return {'acc': cls._acc,
                'jmp': cls._jmp,
                'nop': cls._nop,
                'hcf': cls._hcf}[key]

    def _acc(self, value):
        self.acc += value
        self.ip += 1

    def _jmp(self, value):
        self.ip += value

    def _nop(self, value):
        self.ip += 1

    def _hcf(self, value):
        self.halted = True

    def step(self):
        # Each memory cell is setup as (method, value)
        self.memory[self.ip][0](self, self.memory[self.ip][1])

    def run_safe(self):
        visited_instructions = set()
        try:
            while self.ip not in visited_instructions:
                visited_instructions.add(self.ip)
                self.step()
            if self.halted:
                return
            else:
                raise self.InfiniteLoop(f"Infinite Loop detected at {self.ip}")
        except IndexError:
            raise self.IPOverflow(f"Instruction Pointer overflow to {self.ip}")
