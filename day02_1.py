#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 2 - Challenge 1
https://adventofcode.com/2020/day/2

Solution: 542
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
            min_count = int(match[1])
            max_count = int(match[2])
            character, password = match[3], match[4]
            if min_count <= password.count(character) <= max_count:
                valid_psw += 1
    print(f"\nThere are {valid_psw} valid passwords\n")
    return valid_psw


if __name__ == "__main__":
    main()
