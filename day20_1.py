#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 20 - Challenge 1
https://adventofcode.com/2020/day/20

Solution: 59187348943703
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from collections import namedtuple
from functools import reduce
from aocmodule import sumtuple


VERSORS = [(0, +1), (+1, 0), (0, -1), (-1, 0)]
MATCHDIR = {0: 2, 1: 3, 2: 0, 3: 1}


class Tile():

    Variant = namedtuple('Variant', 'borders tile')

    def __init__(self, tile, header=True, id=0):
        if header:
            self.id = int(tile.pop(0).split()[1][:-1])  # Get id from first row
        else:
            self.id = id
        base_tile = [list(line) for line in tile]
        variants = [self._rotate_tile(base_tile, k=x) for x in range(4)]
        variants += [self._flip_tile(x) for x in variants]
        self.variants = [self.Variant(self._get_borders(x), x) for x in variants]
        self.current_variant = None

    @staticmethod
    def _flip_tile(tile_version):
        return [line[::-1] for line in tile_version]

    @staticmethod
    def _rotate_tile(tile_version, k=1):
        for _ in range(k):
            tile_version = [[line[x] for line in tile_version[::-1]]
                            for x in range(len(tile_version[0]))]
        return tile_version

    @staticmethod
    def _get_borders(tile_version):
        top = tile_version[0]
        bot = tile_version[-1]
        lef = [line[0] for line in tile_version]
        rig = [line[-1] for line in tile_version]
        return tuple(''.join(x) for x in (top, rig, bot, lef))

    def match(self, bordermap):
        for variant in self.variants:
            for i in range(4):
                if variant.borders[MATCHDIR[i]] in bordermap[i]:
                    self.current_variant = variant
                    return i, variant.borders[MATCHDIR[i]]
        raise IndexError


def read_input(ifile):
    tiles = []
    tile = []
    with open(ifile) as file:
        for line in file:
            line = line.strip()
            if line:
                tile.append(line)
            else:
                tiles.append(Tile(tile))
                tile = []
        tiles.append(Tile(tile))  # HACK for the final tile
    return tiles


def arrange_tiles(tiles):
    picture = {}
    starting_tile = tiles.pop()
    starting_tile.current_variant = starting_tile.variants[0]
    picture[(0, 0)] = starting_tile
    bordermap = [{starting_tile.current_variant.borders[x]: VERSORS[x]}
                 for x in range(4)]
    while tiles:
        for tile in tiles:
            try:
                i, edge = tile.match(bordermap)
            except IndexError:
                continue
            # Found a matching tile!
            new_node = bordermap[i][edge]
            bordermap[i].pop(edge)
            picture[new_node] = tile
            for j in range(4):
                if j != MATCHDIR[i]:
                    bordermap[j][tile.current_variant.borders[j]] = \
                        sumtuple(new_node, VERSORS[j])
            break
        tiles.remove(tile)
    minx, miny = (min(x[k] for x in picture) for k in range(2))
    offset = (-minx, -miny)
    new_picture = {}
    for tile_coords in picture.keys():
        new_picture[sumtuple(tile_coords, offset)] = picture[tile_coords]
    nx, ny = (max(x[k] for x in new_picture) + 1 for k in range(2))
    return new_picture, (nx, ny)


def main(ifile='inputs/day_20_input.txt'):
    """We rely on the strong assumption that each edge is unique
    """
    tiles = read_input(ifile)
    picture, (nx, ny) = arrange_tiles(tiles)
    corner_tiles_coords = [(0, 0), (nx-1, 0), (0, ny-1), (nx-1, ny-1)]
    result = reduce(lambda x, y: x * y,
                    (picture[coords].id for coords in corner_tiles_coords))
    print(f"\nThe product of the corner tiles IDs is {result}\n")
    return result


if __name__ == "__main__":
    main()
