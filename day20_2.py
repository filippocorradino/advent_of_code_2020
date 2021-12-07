#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 20 - Challenge 2
https://adventofcode.com/2020/day/20

Solution: 1565
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


import re
from functools import reduce
from day20_1 import Tile, read_input, arrange_tiles


SEA_MONSTER = ['                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ']


def monster_regex(monster, line_len):
    regex = '(?=('
    for i, line in enumerate(monster):
        line = line.replace(' ', '.')
        regex += line
        if i + 1 < len(monster):
            regex += ''.join(('.{', f'{line_len-len(line)}', '}'))
    regex += '))'
    return re.compile(regex)


def trim_tile(tile):
    tile = [x[1:-1] for x in tile[1:-1]]
    return tile


def join_tiles_horz(sx, dx):
    return [x + y for x, y in zip(sx, dx)]


def join_tiles_vert(dn, up):
    return up + dn


def main(ifile='inputs/day_20_input.txt'):
    tiles = read_input(ifile)
    picture, (nx, ny) = arrange_tiles(tiles)
    # FIXME: joined picture doesn't come out right
    for tile_coord in picture:
        picture[tile_coord] = trim_tile(picture[tile_coord].current_variant.tile)
    supertile = Tile(
        reduce(join_tiles_vert,
               (reduce(join_tiles_horz,
                       (picture[(x, y)] for x in range(nx)))
                for y in range(ny))),
        header=False)
    line_len = len(supertile.variants[0].tile[0])
    monster = monster_regex(SEA_MONSTER, line_len)
    monster_indices = [m.start() + i*line_len
                       for i, line in enumerate(SEA_MONSTER)
                       for m in re.finditer('#', line)]
    for variant in supertile.variants:
        oneliner = ''.join(''.join(x) for x in variant.tile)
        matches = [m.start() for m in re.finditer(monster, oneliner)]
        if matches:
            # Counting robust against overlapping monsters
            monster_hash = set()
            for index in matches:
                monster_hash.update(x + index for x in monster_indices)
            supertile_hash = oneliner.count('#')
            result = supertile_hash - len(monster_hash)
            break

    print(f"\nA total of {result} # are not part of any sea monster\n")
    return result


if __name__ == "__main__":
    main()
