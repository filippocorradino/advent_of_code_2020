#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Tests

Simple test script, nothing fancy
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"

import unittest


class TestResults(unittest.TestCase):

    solutions = {'day01_1': 838624,
                 'day01_2': 52764180,
                 'day02_1': 542,
                 'day02_2': 360,
                 'day03_1': 232,
                 'day03_2': 3952291680,
                 'day04_1': 222,
                 'day04_2': 140,
                 'day05_1': 890,
                 'day05_2': 651,
                 'day06_1': 6763,
                 'day06_2': 3512}

    def test_results(self):
        """
        Test all challenges scripts results
        """
        for script in self.solutions:
            print("Testing {0}.py...".format(script))
            with self.subTest(i=script):
                module = __import__(script)
                self.assertEqual(module.main(), self.solutions[script])
        print("All done")


if __name__ == '__main__':
    unittest.main()
