#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 1 - Challenge 1
https://adventofcode.com/2020/day/1

Solution: 838624
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from itertools import combinations


def main(ifile="inputs/day_01_input.txt", total=2020):
    with open(ifile) as file:
        entries = [int(line) for line in file]
    x_sol, y_sol = next((x, y) for x, y in combinations(entries, 2)
                        if x + y == total)
    output = x_sol * y_sol
    print(f"\nThe two entries are {x_sol}, {y_sol}, with product: {output}\n")
    return output


if __name__ == "__main__":
    main()
