"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""
__author__ = 'cjpowell'


def main():
    power = input('Enter the power: ')
    number = str(2 << power - 1)
    result = 0
    for index in number:
        result += int(index)
    print result

if __name__ == '__main__':
    main()