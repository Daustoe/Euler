# coding=utf-8
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
__author__ = 'cjpowell'


def collatz(value):
    steps = 1
    while value != 1:
        if value % 2 == 0:
            value /= 2
        else:
            value = 3 * value + 1
        steps += 1
    return steps


def main():
    max_steps = 0
    max_value = 0
    limit = input('Enter a limit:')
    for number in range(1, limit):
        steps = collatz(number)
        if steps > max_steps:
            max_steps = steps
            max_value = number
    print max_value

if __name__ == '__main__':
    main()