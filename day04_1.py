#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 4 - Challenge 1
https://adventofcode.com/2020/day/4

Solution: 222
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def validate_passports_batch(ifile, rules):
    with open(ifile) as file:
        raw_text = file.read()
    passports = raw_text.split('\n\n')
    valid_passports = 0
    for passport in passports:
        if all(rule(passport) for rule in rules):
            valid_passports += 1
    return valid_passports


def main(ifile='inputs/day_04_input.txt'):
    fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

    def rule(pattern):
        return lambda x: pattern in x

    rules = [rule(field) for field in fields]
    valid_passports = validate_passports_batch(ifile, rules)
    print(f"\nThere are {valid_passports} valid passports\n")
    return valid_passports


if __name__ == "__main__":
    main()
