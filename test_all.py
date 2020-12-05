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
                 'day01_2': 52764180}

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
