# coding=utf-8
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
__author__ = 'cjpowell'


def count_paths(size):
    cube = [1] * size
    for i in range(size):
        for j in range(i):
            cube[j] += cube[j - 1]
        cube[i] = 2 * cube[i - 1]
    return cube[size - 1]


def main():
    length = input('Enter length of cube: ')
    print count_paths(length)


if __name__ == '__main__':
    main()