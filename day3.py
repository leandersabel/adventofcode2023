# https://adventofcode.com/2023/day/3

from solution import Solution
import copy


class Day3Solution(Solution):

    def parse_input(self):
        return [list(line) for line in self.input_data.split('\n')]

    def solve_part1(self):
        symbols = set('#$%&*+-/=?@')
        schematic = copy.deepcopy(self.parsed_input)
        numbers = []

        for r, row in enumerate(schematic):
            for c, val in enumerate(row):
                if val in symbols:
                    numbers.extend(scan_neighbours(schematic, r, c))

        return sum(numbers)

    def solve_part2(self):
        schematic = copy.deepcopy(self.parsed_input)
        gears = []

        for r, row in enumerate(schematic):
            for c, val in enumerate(row):
                if val == '*':
                    local_numbers = scan_neighbours(schematic, r, c)

                    if len(local_numbers) == 2:
                        gears.append(int(local_numbers[0]) * int(local_numbers[1]))

        return sum(gears)


def scan_neighbours(schematic, r, c):
    numbers = []

    # Input does not have symbols in the border rows/columns, so it is "safe" to not check bounds
    if str.isdigit(schematic[r - 1][c - 1]):  # Top left
        numbers.append(get_number(schematic, r - 1, c - 1))

    if str.isdigit(schematic[r][c - 1]):  # Left
        numbers.append(get_number(schematic, r, c - 1))

    if str.isdigit(schematic[r + 1][c - 1]):  # Bottom left
        numbers.append(get_number(schematic, r + 1, c - 1))

    if str.isdigit(schematic[r - 1][c]):  # Top
        numbers.append(get_number(schematic, r - 1, c))

    if str.isdigit(schematic[r + 1][c]):  # Bottom
        numbers.append(get_number(schematic, r + 1, c))

    if str.isdigit(schematic[r - 1][c + 1]):  # Top right
        numbers.append(get_number(schematic, r - 1, c + 1))

    if str.isdigit(schematic[r][c + 1]):  # Right
        numbers.append(get_number(schematic, r, c + 1))

    if str.isdigit(schematic[r + 1][c + 1]):  # Bottom right
        numbers.append(get_number(schematic, r + 1, c + 1))

    return numbers


def get_number(schematic, r, c):
    # Find the first column that is not a digit anymore
    while 0 <= c < len(schematic[0]) and str.isdigit(schematic[r][c]):
        c -= 1

    # Read the number and x-out it's digits
    number = ''
    while c + 1 < len(schematic[0]) and str.isdigit(schematic[r][c + 1]):
        number += schematic[r][c + 1]
        schematic[r][c + 1] = 'x'
        c += 1

    return int(number)


if __name__ == "__main__":
    solution = Day3Solution(day=3, example=None)
    solution.run(part=1)
    solution.run(part=2)
