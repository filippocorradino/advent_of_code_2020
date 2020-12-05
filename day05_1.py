#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 5 - Challenge 1
https://adventofcode.com/2020/day/5

Solution: 890
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def parse_tickets_id(ifile):
    with open(ifile) as file:
        for line in file:
            row = int(line[:7].replace('F', '0').replace('B', '1'), base=2)
            col = int(line[7:].replace('L', '0').replace('R', '1'), base=2)
            yield 8*row + col


def main(ifile='inputs/day_05_input.txt'):
    """
    We'll use the fact that a ticket can be interpreted as two binary numbers
    E.g. FBFBBFF-RLR: FBFBBFF = 1010011 for the row, RLR = 101 for the column
    """
    max_id = max(parse_tickets_id(ifile))
    print(f"\nThe max ticket ID is {max_id}\n")
    return max_id


if __name__ == "__main__":
    main()
