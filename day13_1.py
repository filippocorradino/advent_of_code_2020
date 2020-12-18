#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 13 - Challenge 1
https://adventofcode.com/2020/day/13

Solution: 4938
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from math import ceil


def main(ifile='inputs/day_13_input.txt'):
    with open(ifile) as file:
        min_time = int(file.readline())
        timetable = file.readline()
    periods = [int(t) for t in timetable.split(',') if t != 'x']
    dep_times = [t * ceil(min_time/t) for t in periods]
    ix = dep_times.index(min(dep_times))
    result = (dep_times[ix] - min_time) * periods[ix]
    print(f"\nThe product of bus ID and minimum wait time is: {result}\n")
    return result


if __name__ == "__main__":
    main()
