#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 12 - Challenge 2
https://adventofcode.com/2020/day/12

Solution: 178986
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from aocmodule import GridWalker


def main(ifile='inputs/day_12_input.txt'):
    ship = GridWalker()
    wpt = GridWalker()
    wpt.move(wpt.Directions.EAST, 10)
    wpt.move(wpt.Directions.NORTH, 1)
    actions_dict = {'N': lambda s: wpt.move(wpt.Directions.NORTH, s),
                    'S': lambda s: wpt.move(wpt.Directions.SOUTH, s),
                    'E': lambda s: wpt.move(wpt.Directions.EAST, s),
                    'W': lambda s: wpt.move(wpt.Directions.WEST, s),
                    'L': lambda d: wpt.arc_left(d // 90),
                    'R': lambda d: wpt.arc_right(d // 90),
                    'F': lambda s: ship.move(wpt.position, s)}
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
