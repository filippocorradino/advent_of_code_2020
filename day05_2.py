#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 5 - Challenge 2
https://adventofcode.com/2020/day/5

Solution: 651
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from day05_1 import parse_tickets_id


def main(ifile='inputs/day_05_input.txt', n_seats=1024):
    empty_seats = set(range(n_seats)) ^ set(parse_tickets_id(ifile))
    my_seat = next(x for x in empty_seats
                   if x-1 not in empty_seats and x+1 not in empty_seats)
    print(f"\nMy seat ID is {my_seat}\n")
    return my_seat


if __name__ == "__main__":
    main()
