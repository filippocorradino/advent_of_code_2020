#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 17 - Challenge 1
https://adventofcode.com/2020/day/17

Solution: 291
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from aocmodule import Grid, GollyAutomaton


def run(space, n_steps):
    rule = 'B3/S23'
    automaton = GollyAutomaton(space, rule)
    while n_steps:
        n_steps -= 1
        if any(automaton.space.nodes[x] for x in automaton.space.borders):
            # Live cells have reached the border, extend
            # (Shouldn't happen with pre-expansion)
            space = space.expand(1, lambda _: 0)
            automaton = GollyAutomaton(space, rule)
        next(automaton.generation)
    return space


def hypergolly(ifile, cycles, dimensions):
    symbol_dict = {'.': 0, '#': 1}
    with open(ifile) as file:
        initial_slice = file.read().splitlines()
    for _ in range(dimensions - 2):
        initial_slice = [initial_slice]  # increase dimensionality
    space = Grid.from_nested_sequences(initial_slice, depth=dimensions,
                                       inverse_order=True,
                                       values_map=lambda x: symbol_dict[x])
    space = space.expand(cycles, lambda _: 0)  # Pre-expand by c * cycles
    space = run(space, cycles)
    return sum(space.nodes.values())


def main(ifile='inputs/day_17_input.txt'):
    x = hypergolly(ifile, cycles=6, dimensions=3)
    print(f"\nThe number of live cells is {x}\n")
    return x


if __name__ == "__main__":
    main()
