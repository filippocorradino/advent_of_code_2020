#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 6 - Challenge 2
https://adventofcode.com/2020/day/6

Solution: 3512
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def main(ifile='inputs/day_06_input.txt'):
    with open(ifile) as file:
        raw_text = file.read()
    forms = raw_text.split('\n\n')
    total = 0
    for form in forms:
        personal_answers = (set(x) for x in form.split('\n'))
        total += len(set.intersection(*(x for x in personal_answers)))
    print(f"\nThe sum of all forms count is {total}\n")
    return total


if __name__ == "__main__":
    main()
