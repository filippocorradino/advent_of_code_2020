#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 16 - Challenge 2
https://adventofcode.com/2020/day/16

Solution: 2766491048287
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from copy import deepcopy
from functools import reduce
from day16_1 import read_tickets


def match(possibilities, matchdict={}):
    """Given a list of possible matches for each position,
    it tries to find a global perfect matching via matches DFS.
    """
    n_options = [len(x) for x in possibilities]
    if not any(n_options):
        return matchdict
    # Try all possibilities among the position with the least options
    k = n_options.index(min([x for x in n_options if x > 0]))
    for choice in possibilities[k]:
        new_possibilities = deepcopy(possibilities)  # "Isolate" choices
        matchdict[choice] = k
        for x in new_possibilities:
            try:
                x.remove(choice)
            except ValueError:
                pass
        matching = match(new_possibilities, matchdict)
        if matching:
            return matching
    return {}


def main(ifile='inputs/day_16_input.txt'):
    rules, my_ticket, near_tickets = read_tickets(ifile)
    # Discard invalid tickets
    valid_tickets = []
    for ticket in near_tickets:
        if not [x for x in ticket
                if not any(rule(x) for rule in rules.values())]:
            valid_tickets.append(ticket)
    # Find possible rules for every ticket field, in order
    viable_rules = [[rulename for rulename, rule in rules.items()
                     if all(rule(x) for x in field_values)]
                    for field_values in zip(*valid_tickets)]
    # I could have used a max flow algorithm to find a perfect matching
    # However I went for a custom DFS
    matching = match(viable_rules)
    indexes = [v for k, v in matching.items() if k.startswith('departure')]
    result = reduce(lambda x, y: x*y, [my_ticket[k] for k in indexes])
    print(f"\nThe product of the 'departure' fields is {result}\n")
    return result


if __name__ == "__main__":
    main()
