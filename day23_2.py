#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 23 - Challenge 2
https://adventofcode.com/2020/day/23

Solution: 474747880250
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from day23_1 import play_game


def main(starting_cups='193467258', turns=10000000, n_cups=1000000):
    cups = [int(x) for x in starting_cups] + \
        [x + 1 for x in range(len(starting_cups), n_cups)]
    cups = play_game(cups, turns)
    _ = next(cups)
    cup1 = next(cups)
    cup2 = next(cups)
    result = cup1 * cup2
    print(f"\nThe product of the two cups after 1 is: {result}\n")
    return result


if __name__ == "__main__":
    main()
