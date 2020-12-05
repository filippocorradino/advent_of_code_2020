#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 2 - Challenge 2
https://adventofcode.com/2020/day/2

Solution: 360
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


import re


def main(ifile='inputs/day_02_input.txt'):
    valid_psw = 0
    regex = re.compile(r'(\d+)-(\d+) (\w): (\w*)')
    with open(ifile) as file:
        for line in file:
            match = re.match(regex, line)
            index_1 = int(match[1]) - 1
            index_2 = int(match[2]) - 1
            character, password = match[3], match[4]
            subset = ''.join((password[x] for x in (index_1, index_2)))
            if subset.count(character) == 1:
                valid_psw += 1
    print(f"\nThere are {valid_psw} valid passwords\n")
    return valid_psw


if __name__ == "__main__":
    main()
