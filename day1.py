# https://adventofcode.com/2023/day/1
import re

from solution import Solution


def sum_up(data):
    return sum([int(str(row[0]) + str(row[-1])) for row in data])


class Day1Solution(Solution):

    def solve_part1(self):
        data = [re.sub(r'[^0-9]', '', row) for row in self.input_data.split('\n')]
        return sum_up(data)

    def solve_part2(self):
        data = []

        pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d+))'
        digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                  'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

        for row in self.input_data.split('\n'):
            nums = re.findall(pattern, row)
            data.append(''.join([digits[x] if x in digits.keys() else x for x in nums]))

        return sum_up(data)


if __name__ == "__main__":
    solution = Day1Solution(day=1, example=None)
    solution.run(part=1)
    solution.run(part=2)
