# https://adventofcode.com/2023/day/2
import math
import re

from solution import Solution


class Day2Solution(Solution):

    def parse_input(self):
        games = []

        for game in [(line.split(':')[1].split(';')) for line in self.input_data.split('\n')]:
            dice_raw = [re.findall(r'\d+ [red|green|blue]*', hand) for hand in game]
            dice = [{die.split()[1]: int(die.split()[0]) for die in dice} for dice in dice_raw]
            games.append(dice)

        return games

    def solve_part1(self):
        result = 0

        for i, game in enumerate(self.parsed_input):
            game_possible = True
            for dice in game:
                if dice.get('red', 0) > 12 or dice.get('green', 0) > 13 or dice.get('blue', 0) > 14:
                    game_possible = False

            if game_possible:
                result += i + 1

        return result

    def solve_part2(self):
        result = 0

        for i, game in enumerate(self.parsed_input):
            min_dice = {'red': 0, 'green': 0, 'blue': 0}

            for dice in game:
                min_dice = {die: max(min_dice[die], dice.get(die, 0)) for die in min_dice}

            result += math.prod(min_dice.values())

        return result


if __name__ == "__main__":
    solution = Day2Solution(day=2, example=None)
    solution.run(part=1)
    solution.run(part=2)
