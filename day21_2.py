#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 21 - Challenge 2
https://adventofcode.com/2020/day/21

Solution: vmhqr,qxfzc,khpdjv,gnrpml,xrmxxvn,rfmvh,rdfr,jxh
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from day16_2 import match
from day21_1 import analyze_menu


def main(ifile='inputs/day_21_input.txt'):
    _, _, allergen_index = analyze_menu(ifile)
    matching_vector = []
    for allergen, possibilities in sorted(allergen_index.items()):
        matching_vector.append(list(possibilities))
    matching = match(matching_vector, matchdict={})
    CDIL = ','.join(sorted(matching, key=matching.get))
    print(f"\nThe canonical dangerous ingredient list is {CDIL}\n")
    return CDIL


if __name__ == "__main__":
    main()
