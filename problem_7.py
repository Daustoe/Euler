"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
__author__ = 'cjpowell'


def is_prime(value):
    for num in range(3, int(value**0.5) + 1, 2):
        if value % num == 0:
            return False
    return True


def get_primes(limit):
    primes = 0
    current = 0
    while primes != limit:
        current += 2
        if is_prime(current):
            primes += 1
    return current


def main():
    limit = input('Enter a limit: ')
    print get_primes(limit)

if __name__ == '__main__':
    main()