import itertools


def different_characters(str1, str2):
    number_of_different_characters = 0
    index = 0
    for char in str1:
        if str2[index] != char:
            number_of_different_characters += 1
        index += 1
    return number_of_different_characters


def same_characters(str1, str2):
    index = 0
    output = ""
    for char in str1:
        if str2[index] == char:
            output += char
        index += 1
    return output

def main():

    with open('day2_puzzle1_input.txt', 'r') as inputfile:
        lines = inputfile.read().splitlines()

    for a, b in itertools.combinations(lines, 2):
        if different_characters(a, b) == 1:
            same_chars = same_characters(a, b)
            print("A: {} B: {} Common: {}".format(a, b, same_chars))


if __name__ == "__main__":
    main()
