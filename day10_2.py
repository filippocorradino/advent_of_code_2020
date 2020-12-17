#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 10 - Challenge 2
https://adventofcode.com/2020/day/10

Solution: 1727094849536
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from itertools import accumulate, combinations
from day10_1 import get_adapter_chain_diff


def all_combinations(sequence):
    for r in range(len(sequence)+1):
        for c in combinations(sequence, r):
            yield c


def main(ifile='inputs/day_10_input.txt'):
    """
    Let the chain of adapters joltage rating be a[i],
    with i = 0 being the outlet and i = N being the built-in adapter.
    Let the chain of joltage differences be d[i] = a[i] - a[i-1]
    Then, d[j] is the joltage difference handled by the j-th adapter,
    with j = 1 being the first adapter and j = N being the built-in adapter.
    It is trivial to observe that if d[j] = 3, then adapters j, j-1 are both
    mandatory (this by the way also automatically makes the built-in adapter
    mandatory, since by problem definition d[N] = 3).
    We can therefore split the d-chain in M sub-chains d_xy[k] of adjacent d[j]
    between d[x], d[y] such that d[x] = d[y] = 3 while d_xy[k] < 3 for each k.
    These correspond to adapters sub-chains, the extremities of which are to be
    considered fixed, while we can scroll through all possible combinations of
    "internal" adapters, from adapter x+1 to y-1, and filter the valid ones.
    We then just need to cumulatively multiply these combinations across all
    identified sub-chains (since they are independent).
    TODO: Consider if solving with Graphs would be neater
    """
    differences = get_adapter_chain_diff(ifile)
    # Pass from string and split in sub-chains with all d[j] < 3
    differences_str = ("".join(map(str, differences)))
    sub_chains_str = [s for s in differences_str.split('3') if s]
    # Count the combinations in each sub-chain and multiply them together
    total_combinations = 1
    known_sub_chains = {}
    for sub_chain_str in sub_chains_str:
        try:
            # Let's save some effort if we found the same sub-chain before
            total_combinations *= known_sub_chains[sub_chain_str]
        except KeyError:
            # New sub-chain of which we need to evaluate valid combinations
            current_combinations = 0
            sub_chain = list(map(int, sub_chain_str))
            # Reconstruct "local" adapters values from a[x] to a[y]
            # We use a local reference so that a[x] = 0
            adapters = [0] + list(accumulate(sub_chain))
            internals = adapters[1:-1]
            # We cycle through ALL combinations of internal adapters and try
            # to remove each one from the sub-chain, and see if it's still OK
            for c in all_combinations(internals):
                test_chain = [a for a in adapters if a not in c]
                if all((y - x) <= 3
                        for x, y in zip(test_chain[:-1], test_chain[1:])):
                    current_combinations += 1
            # Tally up
            total_combinations *= current_combinations
            known_sub_chains[sub_chain_str] = current_combinations

    print(f"\nThe number of viable combinations is: {total_combinations}\n")
    return total_combinations


if __name__ == "__main__":
    main()
