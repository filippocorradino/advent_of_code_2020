#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 10 - Challenge 1
https://adventofcode.com/2020/day/10

Solution: 2368
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def get_adapter_chain_diff(ifile):
    with open(ifile) as file:
        adapters = [int(line) for line in file]
    adapters.append(0)  # Add charging outlet
    adapters.sort()  # If a valid chain exists, then this surely is valid
    adapters.append(adapters[-1] + 3)  # Add built-in adapter
    differences = [y - x for x, y in zip(adapters[:-1], adapters[1:])]
    return differences


def main(ifile='inputs/day_10_input.txt'):
    differences = get_adapter_chain_diff(ifile)
    result = differences.count(1) * differences.count(3)
    print(differences)
    print(f"\nThe product of the 1 and 3 differences is: {result}\n")
    return result


if __name__ == "__main__":
    main()
