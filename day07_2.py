#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 7 - Challenge 1
https://adventofcode.com/2020/day/7

Solution: 35487
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from day07_1 import build_suitcase_tree


def count_all_branches_weighted(tree, node):
    branches = tree.edges[node].keys()
    if branches:
        return sum(tree.edges[node][branch] *
                   count_all_branches_weighted(tree, branch)
                   for branch in branches) + 1
        # + 1 because we need to count "node" as well
    else:
        return 1


def main(ifile='inputs/day_07_input.txt', mybag='shiny gold'):
    suitcase_tree = build_suitcase_tree(ifile)
    n_bags = count_all_branches_weighted(suitcase_tree, mybag) - 1
    # - 1 because we're also counting mybag otherwise
    print(f"\nBags within a single {mybag} bag: {n_bags}\n")
    return n_bags


if __name__ == "__main__":
    main()
