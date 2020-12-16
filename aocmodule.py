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
