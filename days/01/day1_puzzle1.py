

def main():

    initial = 0
    with open('day1_puzzle1_input.txt', 'r') as inputFile:
        lines = inputFile.readlines()
        for line in lines:
            initial = initial + int(line)

        print("Output: {}".format(initial))


if __name__ == "__main__":
    main()
