#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 7 - Challenge 1
https://adventofcode.com/2020/day/7

Solution: 252
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


import re
from aocmodule import Graph


def build_suitcase_tree(ifile):
    suitcase_tree = Graph()
    regex = re.compile(r'(\d+) (.*?) bags?')
    with open(ifile) as file:
        for line in file:
            mother_bag, contents = line.split(' bags contain ')
            for number, child_bag in re.findall(regex, contents):
                suitcase_tree.add_edge(mother_bag, child_bag, int(number))
    return suitcase_tree


def main(ifile='inputs/day_07_input.txt', mybag='shiny gold'):
    suitcase_tree = build_suitcase_tree(ifile)
    n_bags = len(suitcase_tree.find_all_upstream(mybag))
    print(f"\nBag colors which can contain at least one {mybag} bag: "
          f"{n_bags}\n")
    return n_bags


if __name__ == "__main__":
    main()
