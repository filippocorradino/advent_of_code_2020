#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 24 - Challenge 1
https://adventofcode.com/2020/day/24

Solution: 373
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


import re
from aocmodule import GridWalker


# We use a coordinate system with x and y axis forming a 120 deg angle
versor_map = {'nw': complex(0, +1),
              'ne': complex(+1, +1),
              'e': complex(+1, 0),
              'se': complex(0, -1),
              'sw': complex(-1, -1),
              'w': complex(-1, 0)}


def floorplan(ifile):
    tiler = GridWalker(cw_complex_versor_map=versor_map)
    turned_tiles = set()
    regex = re.compile(r'nw|ne|e|se|sw|w')
    with open(ifile) as file:
        for line in file:
            for step in re.findall(regex, line):
                tiler.move(step)
            if tiler.position in turned_tiles:
                turned_tiles.remove(tiler.position)
            else:
                turned_tiles.add(tiler.position)
            tiler.reset()
    return turned_tiles


def main(ifile='inputs/day_24_input.txt'):
    n_turned_tiles = len(floorplan(ifile))
    print(f"\nA total of {n_turned_tiles} tiles have been turned\n")
    return n_turned_tiles


if __name__ == "__main__":
    main()
