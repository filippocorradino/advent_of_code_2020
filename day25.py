#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 25
https://adventofcode.com/2020/day/25

Solution: 17673381
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


DIVISOR = 20201227
SUBJECT = 7


def transform(subject_number, loops, divisor=DIVISOR):
    num = 1
    for _ in range(loops):
        num = (subject_number * num) % divisor
    return num


def find_loop_size(public_key, subject_number=SUBJECT, divisor=DIVISOR):
    num = 1
    loop = 0
    while num != public_key:
        num = (subject_number * num) % divisor
        loop += 1
    return loop


def main(ifile='inputs/day_25_input.txt'):
    with open(ifile) as file:
        public_keys = [int(line) for line in file]
    encryption_key = transform(public_keys[0], find_loop_size(public_keys[1]))
    print(f"\nThe encryption key is: {encryption_key}\n")
    return encryption_key


if __name__ == "__main__":
    main()
