#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Day 13 - Challenge 2
https://adventofcode.com/2020/day/13

Solution: 230903629977901
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from functools import reduce
from itertools import combinations
from math import gcd


def main(ifile='inputs/day_13_input.txt'):
    """
    We'll obtain a set of tuples (m_i, a_i) for which we need to then solve
    the following system of congruences for n:

        n ≡ a_1 (mod m_1)
        n ≡ a_2 (mod m_2)
        ...
        n ≡ a_R (mod m_R)

    Fortunately, the Chinese Remainder Theorem comes to the rescue, assuming
    that GCD(m_i) = 1

    Quick refresher of CRT:
    -----------------------
    Let M = m_1*m_2*...*m_R
    Let M_k = M / m_k for each k = 1..R
    Then note that GCD(M_k, M) = 1, while M_h ≡ 0 (mod m_k) for each h != k

    Let y_k be an inverse of M_k modulo m_k, i.e. y_k * M_k ≡ 1 (mod m_k)
    Then let's calculate the solution as follows:

    n = a_1*M_1*y_1 + a_2*M_2*y_2 + ... + a_R*M_R*y_R

    Remembering that M_h ≡ 0 (mod m_k) for h != k, it's easy to see that:
    n ≡ a_k*M_k*y_k ≡ a_k (mod m_k)

    It can also be shown that n is unique mod M.
    # TODO: Generalize if GCD(m_i) != 1
    """
    with open(ifile) as file:
        _ = file.readline()
        timetable = file.readline()
    # Obtain system coefficients (m_i, a_i)
    system = [(int(t), -i)
              for i, t in enumerate(timetable.split(',')) if t != 'x']
    m_i, a_i = zip(*system)
    for c in combinations(m_i, 2):
        assert gcd(c[0], c[1]) == 1
    # We can apply CRT
    n = 0
    M = reduce(lambda x, y: x * y, m_i)
    for m_k, a_k in system:
        M_k = M // m_k
        y_k = pow(M_k, -1, m_k)  # Inverse of Mk modulo mk
        n += a_k * M_k * y_k
    result = n % M
    print(f"\nThe minimum time at which the condition happens is: {result}\n")
    return result


if __name__ == "__main__":
    main()
