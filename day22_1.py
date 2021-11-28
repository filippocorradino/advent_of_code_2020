#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 22 - Challenge 1
https://adventofcode.com/2020/day/22

Solution: 32448
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


def parse_input(ifile):
    hands = []
    with open(ifile) as file:
        for _ in range(2):  # Only 2 players allowed
            _ = file.readline()  # Player name
            cards = []
            while line := file.readline().strip():
                cards.append(int(line))
            hands.append(cards)
    return hands


def play_combat(hands):
    while all(hands):
        deal = [hand.pop(0) for hand in hands]
        winner = deal.index(max(deal))
        hands[winner] += sorted(deal, reverse=True)
    return hands, winner


def score_game(hands, winner):
    hands[winner].reverse()
    score = sum((i+1) * v for i, v in enumerate(hands[winner]))
    return score


def main(ifile='inputs/day_22_input.txt'):
    score = score_game(*play_combat(parse_input(ifile)))
    print(f"\nThe winner's score is {score}\n")
    return score


if __name__ == "__main__":
    main()
