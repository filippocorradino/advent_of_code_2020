#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 14 - Challenge 1
https://adventofcode.com/2020/day/14

Solution: 8566770985168
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def input_parser(ifile):
    with open(ifile) as file:
        for line in file:
            lhs, rhs = line.split(' = ')
            if lhs == 'mask':
                mask = rhs[:-1]  # Remove final \n
                mask_not0 = int(mask.replace('X', '1'), 2) & ((1 << 36) - 1)
                mask_all1 = int(mask.replace('X', '0'), 2)
            else:
                address = int(lhs[4:-1])  # lhs: 'mem[address]'
                yield (mask, mask_not0, mask_all1, address, rhs)


def main(ifile='inputs/day_14_input.txt'):
    memory = {}
    for line in input_parser(ifile):
        _, mask_not0, mask_all1, address, rhs = line
        value = int(rhs) & mask_not0 | mask_all1
        memory[address] = value
    total = sum(memory.values())
    print(f"\nThe sum of all values in memory is {total}\n")
    return total


if __name__ == "__main__":
    main()
