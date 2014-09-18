"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
__author__ = 'cjpowell'


def find_factor_pairs(value):
    pairs = []
    for each in range(1, int(value**0.5)+1):
        if value % each == 0:
            pairs.append((each, value / each))
    return pairs


def dickson_method(limit):
    for value in range(2, limit/2, 2):
        for pair in find_factor_pairs(value**2/2):
            a = value + pair[0]
            b = value + pair[1]
            c = value + pair[0] + pair[1]
            if a + b + c == limit:
                print (a, b, c)
                return a * b * c
    return 0


def main():
    limit = input('Enter a sum to check: ')
    print dickson_method(limit)

if __name__ == '__main__':
    main()