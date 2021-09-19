#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 12 - Challenge 1
https://adventofcode.com/2020/day/12

Solution: 2879
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from aocmodule import GridWalker


def main(ifile='inputs/day_12_input.txt'):
    ship = GridWalker(GridWalker.Directions.EAST)
    actions_dict = {'N': lambda s: ship.move(ship.Directions.NORTH, s),
                    'S': lambda s: ship.move(ship.Directions.SOUTH, s),
                    'E': lambda s: ship.move(ship.Directions.EAST, s),
                    'W': lambda s: ship.move(ship.Directions.WEST, s),
                    'L': lambda d: ship.turn_left(d // 90),
                    'R': lambda d: ship.turn_right(d // 90),
                    'F': lambda s: ship.advance(s)}
    with open(ifile) as file:
        for line in file:
            action, steps = line[0], int(line[1:])
            actions_dict[action](steps)
    distance = sum(abs(x) for x in ship.position)
    print(f"\nThe Manhattan distance to the final position {ship.position} "
          f"is {distance}\n")
    return distance


if __name__ == "__main__":
    main()
