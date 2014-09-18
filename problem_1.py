"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""
__author__ = 'cjpowell'


def sum_multiples(limit, multiples):
    results = 0
    for num in range(1, limit):
        for multiple in multiples:
            if num % multiple == 0:
                results += num
                break
    return results


def main():
    limit = input('Enter a limit: ')
    print sum_multiples(limit, [3, 5])

if __name__ == '__main__':
    main()