#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 9 - Challenge 1
https://adventofcode.com/2020/day/9

Solution: 257342611
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def find_invalid(xmas, preamble):
    for i, value in enumerate(xmas[preamble:]):
        pool = set(xmas[i:i+preamble])  # "preamble" items before current value
        if all((value - x not in pool) for x in pool):
            return value
    raise RuntimeError("Didn't find any invalid number")


def main(ifile='inputs/day_09_input.txt', preamble=25):
    with open(ifile) as file:
        xmas = [int(line) for line in file]
    value = find_invalid(xmas, preamble)
    print(f"\nFirst value to break the XMAS rule: {value}\n")
    return value


if __name__ == "__main__":
    main()
