import re


def main():
    with open("data.txt", "r") as f:
        lines = f.read().split("\n")

    pattern = re.compile(r'(Card\s*(\d*):)')

    result = 0

    for card in lines:
        card_without_no = re.sub(pattern, "", card).split(" ")[1:]
        pipe_idx = card_without_no.index("|")

        winning_numbers, other_numbers = card_without_no[:pipe_idx], card_without_no[pipe_idx+1:]
        winning_numbers = {int(number.strip()) for number in winning_numbers if number}
        other_numbers = {int(number.strip()) for number in other_numbers if number}

        if other_numbers & winning_numbers:
            result += 2 ** (len(other_numbers & winning_numbers) - 1)

    return result


print(main())
