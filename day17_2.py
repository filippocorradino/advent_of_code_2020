#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 17 - Challenge 2
https://adventofcode.com/2020/day/17

Solution: 1524
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from day17_1 import hypergolly


def main(ifile='inputs/day_17_input.txt'):
    x = hypergolly(ifile, rule='B3/S23', cycles=6, dimensions=4)
    print(f"\nThe number of live cells is {x}\n")
    return x


if __name__ == "__main__":
    main()
