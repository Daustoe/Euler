"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
__author__ = 'cjpowell'


def is_palindrome(value):
    value = str(value)
    for index in range(len(value)/2):
        if value[index] != value[-index - 1]:
            return False
    return True


def generate_numbers():
    results = set()
    for value_1 in range(999):
        for value_2 in range(999):
            results.add(value_1 * value_2)
    results = reversed(sorted(results))
    for each in results:
        if is_palindrome(each):
            return each


def main():
    print generate_numbers()

if __name__ == '__main__':
    main()