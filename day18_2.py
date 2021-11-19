#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 18 - Challenge 2
https://adventofcode.com/2020/day/18

Solution: 33331817392479
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from operator import add, mul
from day18_1 import solve_homework


def main(ifile='inputs/day_18_input.txt'):
    total = solve_homework(ifile,
                           operators_dict={'+': add, '*': mul},
                           operators_precedence={'+': 1, '*': 0})
    print(f"\nThe sum of all results is {total}\n")
    return total


if __name__ == "__main__":
    main()
