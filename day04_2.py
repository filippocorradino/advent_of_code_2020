#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 4 - Challenge 2
https://adventofcode.com/2020/day/4

Solution: 140
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


import re
from day04_1 import validate_passports_batch


def make_rule(regex, minimum=None, maximum=None):
    def rule(text):
        result = re.search(regex, text)
        if result:
            if minimum is not None:
                if int(result.groups()[0]) < minimum:
                    return False
            if maximum is not None:
                if int(result.groups()[0]) > maximum:
                    return False
            # Match but no value to be checked
            return True
        # No match
        return False
    return rule


def or_rules(rule1, rule2):
    def rule(text):
        return rule1(text) or rule2(text)
    return rule


def main(ifile='inputs/day_04_input.txt'):
    rules = [make_rule(re.compile(r'byr:(\d{4})(\s|$)'), 1920, 2020),
             make_rule(re.compile(r'iyr:(\d{4})(\s|$)'), 2010, 2020),
             make_rule(re.compile(r'eyr:(\d{4})(\s|$)'), 2020, 2030),
             or_rules(
                 make_rule(re.compile(r'hgt:(\d+)cm(\s|$)'), 150, 193),
                 make_rule(re.compile(r'hgt:(\d+)in(\s|$)'), 59, 76)
                 ),
             make_rule(re.compile(r'hcl:#[0-9,a-f]{6}(\s|$)')),
             make_rule(re.compile(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)')),
             make_rule(re.compile(r'pid:\d{9}(\s|$)'))]
    valid_passports = validate_passports_batch(ifile, rules)
    print(f"\nThere are {valid_passports} valid passports\n")
    return valid_passports


if __name__ == "__main__":
    main()
