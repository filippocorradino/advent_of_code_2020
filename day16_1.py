#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 16 - Challenge 1
https://adventofcode.com/2020/day/16

Solution: 27898
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


import re


def read_tickets(ifile):
    rules = {}
    regex = re.compile(r'(\d+-\d+)')

    def rule_factory(limits):
        # We "freeze" limits for the rule by passing through this scope
        return lambda x: any(lim[0] <= x <= lim[1] for lim in limits)

    with open(ifile) as file:
        # Rule mode
        while line := file.readline().strip():
            rulename, ruletext = line.split(':')
            ranges = re.findall(regex, ruletext)
            limits = [[int(a), int(b)] for r in ranges
                      for a, b in [r.split('-')]]
            rules[rulename] = rule_factory(limits)
        # Ticket mode
        # My ticket
        while line != 'your ticket:':
            line = file.readline().strip()
        while line := file.readline().strip():
            my_ticket = [int(x) for x in line.split(',')]
        # Nearby tickets
        near_tickets = []
        while line != 'nearby tickets:':
            line = file.readline().strip()
        while line := file.readline().strip():
            near_tickets.append([int(x) for x in line.split(',')])

    return rules, my_ticket, near_tickets


def main(ifile='inputs/day_16_input.txt'):
    rules, _, near_tickets = read_tickets(ifile)
    TSER = 0
    for ticket in near_tickets:
        TSER += sum(x for x in ticket if
                    not any(rule(x) for rule in rules.values()))
    print(f"\nThe ticket scanning error rate is {TSER}\n")
    return TSER


if __name__ == "__main__":
    main()
