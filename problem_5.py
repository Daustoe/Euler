"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
__author__ = 'cjpowell'
from functools import reduce
from fractions import gcd


def lcd(a, b):
    return a * b // gcd(a, b)


def main():
    limit = input("Enter a limit: ")
    print reduce(lcd, range(1, limit+1))

if __name__ == '__main__':
    main()