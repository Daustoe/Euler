"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
__author__ = 'cjpowell'


def get_divisor_count(value):
    count = 0
    for num in range(1, int(value**0.5) + 1):
        if value % num == 0:
            count += 2
    return count


def triangle_divisors(limit):
    triangle = 3
    step = 2
    while get_divisor_count(triangle) < limit:
        step += 1
        triangle += step
    return triangle


def main():
    limit = input('Enter a limit: ')
    print triangle_divisors(limit)

if __name__ == '__main__':
    main()