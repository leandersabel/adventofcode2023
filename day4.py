# https://adventofcode.com/2023/day/4

from solution import Solution


class Day4Solution(Solution):

    def parse_input(self):
        cards = []

        for card in [line.split('|') for line in self.input_data.split('\n')]:
            cards.append([{int(num) for num in card[0].split(':')[1].split()}, [int(num) for num in card[1].split()]])

        return cards

    def solve_part1(self):
        result = 0
        for card in self.parsed_input:
            winning_numbers = get_winning_numbers(card)

            if len(winning_numbers) > 0:
                result += 2 ** (len(winning_numbers) - 1)

        return result

    def solve_part2(self):
        card_count = [1] * len(self.parsed_input)

        for card_number, card in enumerate(self.parsed_input):
            winning_numbers = get_winning_numbers(card)

            for i in range(0, len(winning_numbers)):
                card_count[card_number + i + 1] += card_count[card_number]

        return sum(card_count)


def get_winning_numbers(card):
    return [number for number in card[1] if number in card[0]]


if __name__ == "__main__":
    solution = Day4Solution(day=4, example=None)
    solution.run(part=1)
    solution.run(part=2)
