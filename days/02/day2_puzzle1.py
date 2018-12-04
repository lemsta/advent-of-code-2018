from collections import defaultdict


def count_by_letter(word):

    result = defaultdict(int)
    for char in word:
        result[char] = result[char] + 1
    return result


def has_exactly_n_repeats(inputdict, n):
    for letter in inputdict:
        print("inputdict: {}".format(inputdict))
        if inputdict[letter] == n:
            return True
    return False


def main():

    exactly2 = 0
    exactly3 = 0

    with open('day2_puzzle1_input.txt', 'r') as inputfile:
        lines = inputfile.readlines()

    for line in lines:
        result = count_by_letter(line)
        if has_exactly_n_repeats(result, 3):
            exactly3 = exactly3 + 1
        if has_exactly_n_repeats(result, 2):
            exactly2 = exactly2 + 1

    print("Result: {}".format(exactly2 * exactly3))


if __name__ == "__main__":
    main()
