#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 3 - Challenge 2
https://adventofcode.com/2020/day/3

Solution: 3952291680
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from day03_1 import count_trees


def main(ifile='inputs/day_03_input.txt',
         downlist=[1, 1, 1, 1, 2],
         rightlist=[1, 3, 5, 7, 1]):
    with open(ifile) as file:
        treemap = file.read().splitlines()
    output = 1
    for down, right in zip(downlist, rightlist):
        output *= count_trees(treemap, down, right)
    print(f"\nThe product of all trees encountered is {output}\n")
    return output


if __name__ == "__main__":
    main()
