#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 24 - Challenge 2
https://adventofcode.com/2020/day/24

Solution: 3917
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from aocmodule import GollyAutomaton
from day24_1 import versor_map, floorplan


def run(floorplan, cycles, rule='B2/S12'):
    """Golly Automaton running on a sparse hex grid"""
    birth, survive = GollyAutomaton.parse_rule(rule)
    versors = versor_map.values()
    floorplan = set(complex(*x) for x in floorplan)
    for _ in range(cycles):
        to_black = set()
        to_white = set()
        for tile in floorplan:
            neighbours = set(v + tile for v in versors)
            white_neighbours = neighbours - floorplan
            black_neighbours = neighbours - white_neighbours
            if len(black_neighbours) not in survive:
                to_white.add(tile)
            for neighbour in white_neighbours:
                sub_neighbours = set(v + neighbour for v in versors)
                if len(floorplan & sub_neighbours) in birth:
                    to_black.add(neighbour)
        for tile in to_black:
            floorplan.add(tile)
        for tile in to_white:
            floorplan.remove(tile)
    return floorplan


def main(ifile='inputs/day_24_input.txt'):
    n_turned_tiles = len(run(floorplan(ifile), cycles=100))
    print(f"\nA total of {n_turned_tiles} tiles have been turned\n")
    return n_turned_tiles


if __name__ == "__main__":
    main()
