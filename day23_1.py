#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 23 - Challenge 1
https://adventofcode.com/2020/day/23

Solution: 25468379
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def play_game(cups, turns, k=3):
    cups = [x - 1 for x in cups]  # -1 so we can use mod
    n_cups = len(cups)
    next_cups = {cups[i]: cups[(i+1) % n_cups] for i in range(n_cups)}
    current = cups[0]
    side = [0, ] * k  # Preallocate
    for _ in range(turns):
        itercup = next_cups[current]
        for i in range(k):
            side[i] = itercup
            itercup = next_cups[itercup]
        next_cups[current] = itercup
        target = (current - 1) % n_cups
        while target in side:
            target = (target - 1) % n_cups
        aftertarget = next_cups[target]
        next_cups[target] = side[0]
        next_cups[side[-1]] = aftertarget
        current = next_cups[current]

    def cups_gen(start):
        yield start
        cup = next_cups[start]
        while cup != start:
            yield cup
            cup = next_cups[cup]

    for x in cups_gen(0):
        yield x + 1


def main(starting_cups='193467258', turns=100):
    cups = play_game([int(x) for x in starting_cups], turns)
    result = ''.join(str(x) for x in cups)[1:]
    print(f"\nThe cups after 1 are: {result}\n")
    return int(result)


if __name__ == "__main__":
    main()
