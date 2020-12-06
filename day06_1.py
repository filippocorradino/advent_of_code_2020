#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 6 - Challenge 1
https://adventofcode.com/2020/day/6

Solution: 6763
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def main(ifile='inputs/day_06_input.txt'):
    with open(ifile) as file:
        raw_text = file.read()
    forms = raw_text.split('\n\n')
    total = sum(len(set(form.replace('\n', ''))) for form in forms)
    print(f"\nThe sum of all forms count is {total}\n")
    return total


if __name__ == "__main__":
    main()
