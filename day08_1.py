#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 8 - Challenge 1
https://adventofcode.com/2020/day/8

Solution: 1384
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from aocmodule import Processor


def main(ifile='inputs/day_08_input.txt'):
    handheld = Processor.load_from_file(ifile)
    try:
        handheld.run_safe()
    except Processor.InfiniteLoop:
        result = handheld.acc
    else:
        raise RuntimeError("Didn't find any infinite loop")
    print(f"\nAccumulator value just before infinite loop: {result}\n")
    return result


if __name__ == "__main__":
    main()
