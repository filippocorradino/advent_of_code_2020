"""
Advent of Code 2020 - Utilities Module
https://adventofcode.com/2020/

PEP 8 compliant
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


import os
import re
from collections import deque
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

    def __getitem__(self, key):
        return self.nodes[key]

    def __setitem__(self, key, value):
        self.nodes[key] = value

    def add_node(self, node, value=None):
        self.nodes[node] = value
        self.edges[node] = {}

    def add_edge(self, nodeA, nodeB, weight=1, two_ways=False):
        for node in (nodeA, nodeB):
            if node not in self.nodes:
                self.add_node(node)  # Default to a None-valued node
        self.edges[nodeA][nodeB] = weight
        if two_ways:
            self.edges[nodeB][nodeA] = weight

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

    def __init__(self, dimensions, values_map=lambda x: None,
                 neighbourhood=Neighbourhood.MOORE):
        """For each node, its value is set to values_map(node_coordinates)
        """
        super().__init__()
        if len(dimensions) < 2:
            # TODO: manage edge cases with 1D grid
            raise ValueError("'dimensions' must have at least 2 elements")
        self.dimensions = dimensions
        self.neighbourhood = neighbourhood
        self.borders = set()
        for coordinate in product(*(range(d) for d in dimensions)):
            self.add_node(coordinate, values_map(coordinate))
        # Case #1: von Neumann neighbourhood
        if self.neighbourhood == self.Neighbourhood.VON_NEUMANN:
            variations = []
            for i in range(len(dimensions)):
                for step in (-1, +1):
                    variations.append(tuple(step * (i == j)
                                            for j in range(len(dimensions))))
        # Case #2: Moore neighbourhood
        elif self.neighbourhood == self.Neighbourhood.MOORE:
            variations = list(product((-1, 0, +1), repeat=len(dimensions)))
        # Case #N: Unrecognized neighbourhood
        else:
            self.neighbourhood = None
            raise ValueError(f"Unrecognized neighbourhood: {neighbourhood}")
        # Add edges to neighbours for each node
        variations.remove((0,) * len(dimensions))  # discard neighbour = node
        for node in self.nodes:
            for variation in variations:
                neighbour = tuple(x + v for x, v in zip(node, variation))
                if neighbour in self.nodes:
                    self.add_edge(node, neighbour)
                else:
                    # Borders defined as nodes with incomplete neighbourhood
                    self.borders.add(node)

    @classmethod
    def from_nested_sequences(cls, main_sequence, depth,
                              values_map=lambda x: x,
                              neighbourhood=Neighbourhood.MOORE,
                              inverse_order=False):
        """Can generate a grid from input data such as:
        ((1, 2, 3), (4, 5, 6))
        [[1, 2, 3], [4, 5, 6]]
        Sub-sequences at a given level must all be of the same size!
        For each node, its value is set to values_map(sequences_value)
        If inverse_order is True, the innermost subsequence is on the first axis
        (e.g. the sequence above would turn in a (3, 2) grid instead of (2, 3))
        """
        def values(coordinates):
            v = main_sequence
            if inverse_order:
                coordinates = reversed(coordinates)
            for x in coordinates:
                v = v[x]
            return values_map(v)
        dimensions = []
        sub_sequence = main_sequence
        for _ in range(depth):
            dimensions.append(len(sub_sequence))
            sub_sequence = sub_sequence[0]
        if inverse_order:
            dimensions = reversed(dimensions)
        return cls(tuple(dimensions), values, neighbourhood)

    def _2Dsection(self, outer_indices):
        lines = []
        for y in range(self.dimensions[1]):
            lines.append(''.join(str(self[(x, y, *outer_indices)])
                         for x in range(self.dimensions[0])))
        return '\n'.join(lines)

    def __str__(self):
        if len(self.dimensions) == 1:
            # Unused now, will be used when we extend to 1D grids
            return ''.join(str(self[x] for x in range(self.dimensions[0])))
        slices = []
        outer_dimensions = self.dimensions[2:]
        for outer_indices in product(*(range(d) for d in outer_dimensions)):
            if outer_dimensions:
                slices.append('\n'.join((str(outer_indices),
                                        self._2Dsection(outer_indices))))
            else:
                slices.append(self._2Dsection(outer_indices))
        return '\n\n'.join(slices)

    def expand(self, n, values_map=lambda x: None):
        """Returns a new grid expanded by n cells in every direction
        For each new node, its value is set to values_map(coordinates),
        using the new grid coordinate system
        NOTE: old grid coordinates all get increased by n
        """
        def values(coordinates):
            old_coordinates = tuple(x - n for x in coordinates)
            try:
                return self.nodes[old_coordinates]
            except KeyError:
                return values_map(coordinates)
        dimensions = [x + 2*n for x in self.dimensions]
        return self.__class__(tuple(dimensions), values, self.neighbourhood)


class CellularAutomaton():
    """
    Must be based on a Graph object to define nodes and neighbours.
    rule must receive as input the cell value and a list of neighbours values,
    and return the next value of the cell.
    Only isotropic automata are supported for now.
    The space must be initialized with the initial cell values as node values.
    """

    def __init__(self, space, rule):
        self.space = space
        self.rule = rule
        self.cell_engines = \
            [self._step_cell(cell) for cell in self.space.nodes.keys()]
        self.generation = self._step()  # Calling next(generation) steps the CA

    def _step_cell(self, cell):
        # Quasi-coroutine
        neighbours_addresses = self.space.edges[cell].keys()
        while True:
            state = self.space.nodes[cell]
            neighbours = [self.space.nodes[x] for x in neighbours_addresses]
            yield  # End phase 1 - assess
            self.space.nodes[cell] = self.rule(state, neighbours)
            yield  # End phase 2 - update

    def _step(self):
        while True:
            for engine in self.cell_engines:
                next(engine)  # Phase 1 - assess (get state and neighbours)
            for engine in self.cell_engines:
                next(engine)  # Phase 2 - update (propagate next step)
            yield None

    def step(self):
        # Alternative to step the CA
        next(self.generation)


class GollyAutomaton(CellularAutomaton):
    """
    Cellular automaton supporting rules in Golly form (e.g. Life: B3/S23)
    """

    def __init__(self, space, rule):
        self.birth, self.survive = self.parse_rule(rule)

        def golly_rule(cell_value, neighbours_values):
            if cell_value == 0 and sum(neighbours_values) in self.birth:
                return 1
            if cell_value == 1 and sum(neighbours_values) in self.survive:
                return 1
            return 0

        super().__init__(space, golly_rule)

    @staticmethod
    def parse_rule(rule):
        match = re.fullmatch(r'B(\d+)\/S(\d+)', rule)
        return [[int(n) for n in group] for group in match.groups()]


class GridWalker():

    Directions = Enum('Direction', 'NORTH EAST SOUTH WEST')

    def __init__(self, starting_direction=None, starting_position=(0, 0)):
        directions = (self.Directions.NORTH, self.Directions.EAST,
                      self.Directions.SOUTH, self.Directions.WEST)
        versors = (complex(0, +1), complex(+1, 0),
                   complex(0, -1), complex(-1, 0))
        self.versor_map = {k: v for k, v in zip(directions, versors)}
        # Circular list with main directions in CW order (NESW)
        self.orientation = deque(directions)
        self._position = complex(*starting_position)
        if starting_direction:
            # Defaults to North if unset
            while self.orientation[0] != starting_direction:
                self._turn_cw()

    @property
    def position(self):
        return (int(self._position.real), int(self._position.imag))

    def _turn_cw(self, steps=1):
        # This rotates the walker CW by a certain number of steps
        self.orientation.rotate(steps)

    def turn_left(self, steps=1):
        self._turn_cw(steps)

    def turn_right(self, steps=1):
        self._turn_cw(-steps)

    def advance(self, steps=1):
        self.move(self.heading(), steps)

    def move(self, direction, steps=1):
        try:
            self._position += steps * self.versor_map[direction]
        except KeyError:
            self._position += steps * complex(*direction)

    def heading(self):
        return self.orientation[0]

    def _arc_cw(self, quarters=1):
        self._position = self._position * 1j**quarters

    def arc_left(self, quarters=1):
        self._arc_cw(quarters)

    def arc_right(self, quarters=1):
        self._arc_cw(-quarters)


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


class Display():

    def __init__(self, symbol_dict={}, default_pixel=0):
        self.symbol_dict = symbol_dict
        self.default_pixel = default_pixel
        self.pixels = {}
        self.size = None

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def set_size(self, size):
        self.size = size

    def update(self, pixels):
        self.pixels.update(pixels)

    def show(self, legend='', clear=True):
        min_x = min((x for (x, y) in self.pixels))
        min_y = min((y for (x, y) in self.pixels))
        if self.size:
            max_x = min_x + self.size[0]
            max_y = min_y + self.size[1]
        else:
            max_x = max((x for (x, y) in self.pixels))
            max_y = max((y for (x, y) in self.pixels))
        # Reconstruct all symbol values
        rows = []
        for y in range(min_y, max_y + 1):
            row = []
            for x in range(min_x, max_x + 1):
                try:
                    row.append(self.pixels[(x, y)])
                except KeyError:
                    row.append(self.default_pixel)
            rows.append(row)
        # Display
        output = '\n'.join((''.join((self.symbol_dict[j]) for j in row)
                            for row in rows))
        if clear:
            self.clear()
        print("\n{0}\n{1}\n".format(output, legend))

    def refresh(self, pixels, legend='', clear=True):
        self.update(pixels)
        self.show(legend=legend, clear=clear)
