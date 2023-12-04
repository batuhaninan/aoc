import re
from collections import defaultdict


def main():
    with open("data.txt", "r") as f:
        lines = f.read().split("\n")

    pattern = re.compile(r'(Card\s*(\d*):)')

    scratch_cards = defaultdict(lambda: 1)

    for card in lines:
        card_no = int(re.match(pattern, card).group(2))
        card_without_no = re.sub(pattern, "", card).split(" ")[1:]
        pipe_idx = card_without_no.index("|")

        winning_numbers, other_numbers = card_without_no[:pipe_idx], card_without_no[pipe_idx+1:]
        winning_numbers = {int(number.strip()) for number in winning_numbers if number}
        other_numbers = {int(number.strip()) for number in other_numbers if number}

        n_matching_numbers = len(other_numbers & winning_numbers)

        for _ in range(scratch_cards[card_no]):
            for i in range(card_no + 1, card_no + n_matching_numbers + 1):
                scratch_cards[i] += 1

    print(scratch_cards)
    return sum(list(scratch_cards.values()))


print(main())
