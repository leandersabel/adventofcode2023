# https://adventofcode.com/2023/day/7
import copy

from solution import Solution


class Day7Solution(Solution):

    def parse_input(self):
        return [line.split()[:2] for line in self.input_data.split('\n')]

    def solve_part1(self):
        hands = copy.deepcopy(self.parsed_input)

        for hand in hands:
            hand[0] = convert_face_cards(hand[0], joker=False)
            hand.append(get_strength(hand[0]))

        hands_sorted = sorted(hands, key=lambda x: (x[-1], x[0]))
        return sum([int(hand[1]) * (i + 1) for i, hand in enumerate(hands_sorted)])

    def solve_part2(self):
        hands = copy.deepcopy(self.parsed_input)

        for hand in hands:
            hand[0] = convert_face_cards(hand[0], joker=True)
            hand.append(get_strength(hand[0]))

        hands_sorted = sorted(hands, key=lambda x: (x[-1], x[0]))
        return sum([int(hand[1]) * (i + 1) for i, hand in enumerate(hands_sorted)])


def convert_face_cards(hand, joker):
    face_card_values = {'T': 10, 'J': 1 if joker else 11, 'Q': 12, 'K': 13, 'A': 14}
    return [int(card) if card.isdigit() else face_card_values.get(card, None) for card in hand]


def get_strength(hand):
    card_count = {card: hand.count(card) for card in set(hand)}
    jokers = card_count.pop(1, 0)
    counts = sorted(card_count.values(), reverse=True)
    counts = [counts[0] + jokers] + counts[1:] if counts else [jokers]

    if counts[0] == 5:  # Five of a kind
        return 7
    elif counts[0] == 4:  # Four of a kind
        return 6
    if counts[0] == 3 and counts[1] == 2:  # Full house
        return 5
    if counts[0] == 3:  # Three of a kind
        return 4
    if counts[0] == 2 and counts[1] == 2:  # Two pair
        return 3
    if counts[0] == 2:  # One pair
        return 2
    else:  # High card
        return 1


if __name__ == "__main__":
    solution = Day7Solution(day=7, example=None)
    solution.run(part=1)
    solution.run(part=2)

