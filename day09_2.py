#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 9 - Challenge 2
https://adventofcode.com/2020/day/9

Solution: 35602097
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from day09_1 import find_invalid


def main(ifile='inputs/day_09_input.txt', preamble=25):
    with open(ifile) as file:
        xmas = [int(line) for line in file]
    value = find_invalid(xmas, preamble)
    inf = 0
    while inf < len(xmas)-1:
        sup = inf + 2
        currentsum = sum(xmas[inf:sup])
        while currentsum < value and sup < len(xmas):
            sup += 1
            currentsum += xmas[sup-1]
        if currentsum == value:
            min_value = min(xmas[inf:sup])
            max_value = max(xmas[inf:sup])
            result = min_value + max_value
            print(f"\nSum of minimum and maximum value: {result}\n")
            return result
        inf += 1
    raise RuntimeError("Did not find a valid sum")


if __name__ == "__main__":
    main()
