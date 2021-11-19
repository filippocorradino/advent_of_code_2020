#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 18 - Challenge 1
https://adventofcode.com/2020/day/18

Solution: 209335026987
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from operator import add, mul


def simple_shunting_yard(sequence, operators_dict, operators_precedence):
    """Simplified shunting yard algorithm by Djikstra to convert inline to RPN
    """
    outqueue = []
    opstack = []

    def popop():
        op = opstack.pop()
        outqueue.append(operators_dict[op](outqueue.pop(), outqueue.pop()))

    while sequence:
        token = sequence.pop(0)
        if token.isnumeric():
            outqueue.append(int(token))
        elif token == '(':
            opstack.append(token)
        elif token == ')':
            while opstack[-1] != '(':
                popop()
            opstack.pop()  # Pop left parenthesis
        else:
            precedence = operators_precedence[token]
            while (opstack and
                   opstack[-1] != '(' and
                   operators_precedence[opstack[-1]] >= precedence):
                popop()
            opstack.append(token)
    while opstack:
        popop()
    assert len(outqueue) == 1
    return outqueue[0]


def solve_homework(ifile, operators_dict, operators_precedence):
    total = 0
    with open(ifile) as file:
        for line in file:
            line = line.replace('(', ' ( ').replace(')', ' ) ')
            total += simple_shunting_yard(line.split(),
                                          operators_dict, operators_precedence)
    return total


def main(ifile='inputs/day_18_input.txt'):
    total = solve_homework(ifile,
                           operators_dict={'+': add, '*': mul},
                           operators_precedence={'+': 0, '*': 0})
    print(f"\nThe sum of all results is {total}\n")
    return total


if __name__ == "__main__":
    main()
