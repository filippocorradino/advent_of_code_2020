#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 14 - Challenge 2
https://adventofcode.com/2020/day/14

Solution: 4832039794082
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from itertools import chain, combinations
from day14_1 import input_parser


def powerset(inlist):
    return chain.from_iterable(combinations(inlist, r)
                               for r in range(len(inlist) + 1))


def main(ifile='inputs/day_14_input.txt'):
    memory = {}
    memory = {}
    for line in input_parser(ifile):
        mask, mask_not0, _, base_address, rhs = line
        X_values = [2 ** (len(mask)-i-1)
                    for i, c in enumerate(mask) if c == 'X']
        base_address = base_address | mask_not0
        for addendum in powerset(X_values):
            address = base_address - sum(addendum)
            memory[address] = int(rhs)
    total = sum(memory.values())
    print(f"\nThe sum of all values in memory is {total}\n")
    return total


if __name__ == "__main__":
    main()
