# coding=utf-8
"""
The sum of the squares of the first ten natural numbers is,
                        1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                        (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
                        3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
__author__ = 'cjpowell'
from functools import reduce


def square_of_sum(value):
    results = reduce(lambda x, y: x + y, range(value + 1))
    return results**2


def sum_of_squares(value):
    results = 0
    for each in range(value+1):
        results += each**2
    return results


def main():
    limit = input('Enter a limit: ')
    print square_of_sum(limit) - sum_of_squares(limit)

if __name__ == '__main__':
    main()