#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 19 - Challenge 2
https://adventofcode.com/2020/day/19

Solution: 367
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from day19_1 import parse_input, check_rule


def main(ifile='inputs/day_19_input.txt'):
    rules, messages = parse_input(ifile)
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]
    count = len([x for x in messages
                 if len(x) in check_rule(x, [0], rules, '0')])
    print(f"\nThere are {count} messages which fully match the rules\n")
    return count


if __name__ == "__main__":
    main()
