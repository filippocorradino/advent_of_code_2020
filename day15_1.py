#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 15 - Challenge 1
https://adventofcode.com/2020/day/15

Solution: 610

TODO: clean up the logic and improve speed for Part 2 if possible
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def play_game(ifile, n_turns):
    with open(ifile) as file:
        start = file.read()
    read_numbers = [int(x) for x in start.split(',')]
    numbers_turns = {}
    # Initial turns
    turn = 1
    for x in read_numbers[:-1]:
        numbers_turns[x] = turn
        turn += 1
    # Make initial conditions compatible for standard turns algorithm
    x = read_numbers[-1]
    read_numbers = read_numbers[:-1]
    # Standard turns
    while len(read_numbers) < n_turns:
        try:
            last_appearance = numbers_turns[x]
        except KeyError:
            last_appearance = turn
        read_numbers.append(x)
        numbers_turns[x] = turn
        x = turn - last_appearance
        turn += 1
    result = read_numbers[-1]
    print(f"\nThe {n_turns}th number said is {result}\n")
    return result


def main(ifile='inputs/day_15_input.txt'):
    return play_game(ifile, 2020)


if __name__ == "__main__":
    main()
