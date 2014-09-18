"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
(numbers in problem_13_input.txt file)
"""
__author__ = 'cjpowell'


def main():
    number_file = open('problem_13_input.txt', 'r')
    numbers = []
    for line in number_file:
        numbers.append(int(line))

    print str(sum(numbers))[:10]

if __name__ == '__main__':
    main()