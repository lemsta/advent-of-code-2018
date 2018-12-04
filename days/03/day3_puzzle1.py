import re
from collections import defaultdict


class Claim:

    def __init__(self, number, left, top, width, height):
        self.number = number
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def __str__(self):
        return "#{} @ {},{}: {}x{}".format(self.number, self.left, self.top, self.width, self.height)

    def __repr__(self):
        return self.__str__()


def process_claim(line, claim_pattern):
    result = re.match(claim_pattern, line)
    a = Claim(int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4)), int(result.group(5)))
    return a


def claimed(left, top, width, height):
    for x in range(width):
        for y in range(height):
            yield (left + x, top + y)


def main():
    claim_pattern = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    claims = []

    with open('day3_puzzle1_input.txt', 'r') as inputfile:
        lines = inputfile.read().splitlines()

    for line in lines:
        claim = process_claim(line, claim_pattern)
        claims.append(claim)

    sheet = defaultdict(int)
    for claim in claims:
        for point in claimed(claim.left, claim.top, claim.width, claim.height):
            sheet[point] += 1

    overlaps = len(
        [val for point, val in sheet.items() if val > 1]
    )
    print("Total Overlaps: {}".format(overlaps))


if __name__ == "__main__":
    main()
