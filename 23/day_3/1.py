import itertools
import re


def is_special_char(string: str) -> bool:
    if string == ".":
        return False
    specials = re.search("(\W)", string)
    return specials is not None


def main():
    with open("data.txt", "r") as f:
        data = f.read().split("\n")

    box = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
    all_symbols = set()
    result = 0

    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col != "." and not col.isdigit():
                all_symbols.add((i, j))

    for i, row in enumerate(data):
        for match in re.finditer(r"\d+", row):
            neighbours = set()
            for j in range(match.start(), match.end()):
                for bi, bj in box:
                    neighbours.add((bi + i, bj + j))

            if neighbours & all_symbols:
                result += int(match.group(0))

    return result


print(main())
