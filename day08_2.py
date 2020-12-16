#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 8 - Challenge 2
https://adventofcode.com/2020/day/8

Solution: 761
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from copy import deepcopy
from aocmodule import Processor


def fix_program(commands):
    test_commands = deepcopy(commands)
    for i, command in enumerate(commands):
        if command[0] == 'jmp':
            test_commands[i][0] = 'nop'
        elif command[0] == 'nop':
            test_commands[i][0] = 'jmp'
        else:
            continue
        test_program = Processor.load_from_cmd_list(test_commands)
        try:
            test_program.run_safe()
        except (Processor.IPOverflow, Processor.InfiniteLoop):
            test_commands[i][0] = command[0]
            continue
        return test_program
    raise RuntimeError("Didn't find any possible fix for the program")


def main(ifile='inputs/day_08_input.txt'):
    with open(ifile) as file:
        # obtain a list of [opcode, value] pairs in string form
        commands = [line.split() for line in file]
    fixed_handheld = fix_program(commands)
    result = fixed_handheld.acc
    print(f"\nAccumulator value at program termination: {result}\n")
    return result


if __name__ == "__main__":
    main()
