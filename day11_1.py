#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 11 - Challenge 1
https://adventofcode.com/2020/day/11

Solution: 2152
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from aocmodule import Grid, CellularAutomaton, Display


def seating_rule(max_neighbours):
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it,
    the seat becomes occupied.
    If a seat is occupied (#) and max_neighbours or more seats adjacent to it
    are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    Floor (.) never changes; seats don't move, and nobody sits on the floor.
    """
    def rule(state, neighbours):
        occupied_neighbours = sum(n == '#' for n in neighbours)
        if state == 'L' and not occupied_neighbours:
            return '#'
        if state == '#' and occupied_neighbours >= max_neighbours:
            return 'L'
        return state
    return rule


def run_simulation(space, max_neighbours, display):
    simulation = CellularAutomaton(space, seating_rule(max_neighbours))
    screen = Display({'#': '#', 'L': 'L', '.': '.'})

    def count_seats_taken():
        return sum(v == '#' for v in space.nodes.values())

    seats_taken = None
    while count_seats_taken() != seats_taken:
        seats_taken = count_seats_taken()
        next(simulation.generation)
        if display:
            screen.refresh(space.nodes)
    return seats_taken


def main(ifile='inputs/day_11_input.txt', display=False):
    with open(ifile) as file:
        space = Grid.from_nested_sequences(file.read().splitlines(), depth=2,
                                           inverse_order=True)
    seats_taken = run_simulation(space, max_neighbours=4, display=display)
    print(f"\nThere are {seats_taken} seats taken at steady-state\n")
    return seats_taken


if __name__ == "__main__":
    main(display=True)
