#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 3 - Challenge 1
https://adventofcode.com/2020/day/3

Solution: 232
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def count_trees(treemap, down, right):
    height = len(treemap)
    module = len(treemap[0])
    trees = 0
    pos_horz = 0
    for pos_vert in range(down, height, down):  # Start from after first step
        pos_horz = (pos_horz + right) % module
        if treemap[pos_vert][pos_horz] == '#':
            trees += 1
    return trees


def main(ifile='inputs/day_03_input.txt', down=1, right=3):
    with open(ifile) as file:
        treemap = file.read().splitlines()
    trees = count_trees(treemap, down, right)
    print(f"\nWe encountered {trees} trees on the slope: "
          f"down {down} right {right}\n")
    return trees


if __name__ == "__main__":
    main()
