"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
__author__ = 'cjpowell'


def is_prime(value):
    for num in range(3, int(value**0.5) + 1, 2):
        if value % num == 0:
            return False
    return True


def largest_prime_factor(value):
    for num in reversed(range(3, int(value**0.5) + 1, 2)):
        if value % num == 0 and is_prime(num):
            return num
    return 0


def main():
    value = input('Enter a number to test: ')
    print largest_prime_factor(value)

if __name__ == '__main__':
    main()