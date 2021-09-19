#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 11 - Challenge 2
https://adventofcode.com/2020/day/11

Solution: 1937
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from itertools import combinations
from aocmodule import Grid
from day11_1 import run_simulation


def versor(p, q):
    # TODO: create a vector class to simplify all these tuple operations?
    delta = [px-qx for px, qx in zip(p, q)]
    norm = sum(abs(d) for d in delta)  # Use Taxicab to avoid numerical errors
    return [d / norm for d in delta]


def main(ifile='inputs/day_11_input.txt', display=False):
    with open(ifile) as file:
        space = Grid.from_nested_sequences(file.read().splitlines(), depth=2,
                                           inverse_order=True)
    # Let's bridge over the floor nodes
    for node, value in space.nodes.items():
        if value == '.':
            edges_to_del = []
            for nodeA, nodeB in combinations(space.edges[node], 2):
                deltaA = versor(nodeA, node)
                deltaB = versor(nodeB, node)
                if all(a == -b for a, b in zip(deltaA, deltaB)):
                    # Node is on edgeA-edgeB line and can be bridged
                    space.add_edge(nodeA, nodeB, two_ways=True)
                    edges_to_del += [nodeA, nodeB]
            for dest in edges_to_del:
                del space.edges[node][dest]
                del space.edges[dest][node]
    # Now run the simulation
    seats_taken = run_simulation(space, max_neighbours=5, display=display)
    print(f"\nThere are {seats_taken} seats taken at steady-state\n")
    return seats_taken


if __name__ == "__main__":
    main(display=True)
