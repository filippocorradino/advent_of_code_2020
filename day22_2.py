#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 22 - Challenge 2
https://adventofcode.com/2020/day/22

Solution: 32949
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from day22_1 import parse_input, score_game


def play_recursive_combat(hands):
    turns_archive = set()
    while all(hands):
        turn = tuple(tuple(x) for x in hands)
        if turn in turns_archive:
            return hands, 0
        turns_archive.add(turn)
        deal = [hand.pop(0) for hand in hands]
        if all(len(hand) >= deal[i] for i, hand in enumerate(hands)):
            sub_hands = [hand[:d] for hand, d in zip(hands, deal)]
            _, winner = play_recursive_combat(sub_hands)
        else:
            winner = deal.index(max(deal))
        hands[winner] += [deal.pop(winner), deal.pop()]
    return hands, winner


def main(ifile='inputs/day_22_input.txt'):
    score = score_game(*play_recursive_combat(parse_input(ifile)))
    print(f"\nThe winner's score is {score}\n")
    return score


if __name__ == "__main__":
    main()
