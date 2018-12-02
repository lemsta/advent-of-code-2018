import sys

def main():

    initial = 0
    frequency_list = set()

    with open('day1_puzzle1_input.txt', 'r') as inputFile:
        lines = inputFile.readlines()
        while True:
            for line in lines:
                initial = initial + int(line)
                if initial in frequency_list:
                    print("Output: {}".format(initial))
                    sys.exit(0)
                else:
                    frequency_list.add(initial)




if __name__ == "__main__":
    main()
