#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 19 - Challenge 1
https://adventofcode.com/2020/day/19

Solution: 173
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def parse_input(ifile):
    with open(ifile) as file:
        # Rule mode
        rules = {}
        while line := file.readline().strip():
            line = line.replace('"', '')  # Remove " " from "a" and "b"
            ruleid, ruletext = line.split(':')
            rules[ruleid] = [x.split() for x in ruletext.split('|')]
        # Messages mode
        messages = file.read().splitlines()
    return rules, messages


def check_rule(string, indices, rules, ruleid):
    """Tries to match the various options within rules[ruleid], acting from
    string[index] forwards, and returns a list of indices of the positions
    just after valid matches
    """
    new_indices = []
    base = rules[ruleid][0][0]
    if base.isalpha():
        # Base rules
        new_indices += [index + 1 for index in indices if string[index] == base]
        # TODO: do we need to catch IndexErrors in the general case?
    else:
        # Complex rules
        for index in indices:
            if index < len(string):
                for option in rules[ruleid]:
                    sub_indices = [index]
                    for rule in option:
                        sub_indices = check_rule(string, sub_indices,
                                                 rules, rule)
                        if not sub_indices:
                            break
                    new_indices += sub_indices
    return [x for x in new_indices if x <= len(string)]


def main(ifile='inputs/day_19_input.txt'):
    rules, messages = parse_input(ifile)
    count = len([x for x in messages
                 if len(x) in check_rule(x, [0], rules, '0')])
    print(f"\nThere are {count} messages which fully match the rules\n")
    return count


if __name__ == "__main__":
    main()
