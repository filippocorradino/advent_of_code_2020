#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 21 - Challenge 1
https://adventofcode.com/2020/day/21

Solution: 2569
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from collections import defaultdict
from functools import reduce


def parse_menu(ifile):
    allergen_dishes = defaultdict(list)
    dishes = []
    with open(ifile) as file:
        for line in file:
            dish, allergens = line.strip(' )\n').split('(contains ')
            dish = set(dish.split())
            dishes.append(dish)
            allergens = allergens.split(', ')
            for allergen in allergens:
                allergen_dishes[allergen].append(dish)
    return dishes, allergen_dishes


def analyze_menu(ifile):
    dishes, allergen_dishes = parse_menu(ifile)
    allergen_index = {}
    risky_ingredients = set()
    for allergen, risky_dishes in allergen_dishes.items():
        possible_dishes = reduce(lambda x, y: x & y, risky_dishes)
        allergen_index[allergen] = possible_dishes
        risky_ingredients.update(possible_dishes)
    return dishes, risky_ingredients, allergen_index


def main(ifile='inputs/day_21_input.txt'):
    dishes, risky_ingredients, _ = analyze_menu(ifile)
    count = 0
    for dish in dishes:
        count += len(dish - risky_ingredients)
    print(f"\nThe safe ingredients appear {count} times in the menu\n")
    return count


if __name__ == "__main__":
    main()
