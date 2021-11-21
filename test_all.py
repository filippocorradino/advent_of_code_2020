#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2020 - Tests

Simple test script, nothing fancy
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from importlib import import_module
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
                 'day06_2': 3512,
                 'day07_1': 252,
                 'day07_2': 35487,
                 'day08_1': 1384,
                 'day08_2': 761,
                 'day09_1': 257342611,
                 'day09_2': 35602097,
                 'day10_1': 2368,
                 'day10_2': 1727094849536,
                 'day11_1': 2152,
                 'day11_2': 1937,
                 'day12_1': 2879,
                 'day12_2': 178986,
                 'day13_1': 4938,
                 'day13_2': 230903629977901,
                 'day14_1': 8566770985168,
                 'day14_2': 4832039794082,
                 'day15_1': 610,
                 'day15_2': 1407,
                 'day16_1': 27898,
                 'day16_2': 2766491048287,
                 'day17_1': 291,
                 'day17_2': 1524,
                 'day18_1': 209335026987,
                 'day18_2': 33331817392479}

    def test_results(self):
        """
        Test all challenges scripts results
        """
        for script in self.solutions:
            print("Testing {0}.py...".format(script))
            with self.subTest(i=script):
                module = import_module(script)
                self.assertEqual(module.main(), self.solutions[script])
        print("All done")


if __name__ == '__main__':
    unittest.main()
