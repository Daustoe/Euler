"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
__author__ = 'cjpowell'


def sieve_of_eratosthenes(limit):
    results = 0
    multiples = set()
    for num in range(2, limit + 1):
        if num not in multiples:
            results += num
            multiples.update(range(num * num, limit + 1, num))
    return results


def main():
    limit = input('Enter a limit: ')
    print sieve_of_eratosthenes(limit)

if __name__ == '__main__':
    main()