#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 1 - Challenge 2
https://adventofcode.com/2020/day/1

Solution: 52764180
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from itertools import combinations


def main(ifile='inputs/day_01_input.txt', total=2020):
    with open(ifile) as file:
        entries = [int(line) for line in file]
    x_sol, y_sol, z_sol = \
        next((x, y, z) for x, y, z in combinations(entries, 3)
             if x + y + z == total)
    output = x_sol * y_sol * z_sol
    print(f"\nThe three entries are {x_sol}, {y_sol}, {z_sol}, "
          f"with product: {output}\n")
    return output


if __name__ == "__main__":
    main()
