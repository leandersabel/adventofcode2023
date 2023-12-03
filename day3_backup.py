# https://adventofcode.com/2023/day/3

from solution import Solution
import copy


def get_number(schematic, r, i):
    number = ''
    while i < len(schematic[0]) and str.isdigit(schematic[r][i]):
        number += schematic[r][i]
        schematic[r][i] = 'x'
        i += 1
    return number


class Day3Solution(Solution):

    def parse_input(self):
        return [list(line) for line in self.input_data.split('\n')]

    def solve_part1(self):
        symbols = set('#$%&*+-/=?@')
        schematic = copy.deepcopy(self.parsed_input)
        numbers = []

        print(*schematic, sep='\n')

        for r, row in enumerate(schematic):
            for c, val in enumerate(row):
                if val in symbols:
                    # Found symbol. Scan for numbers.
                    # Input does not have symbols in the border rows/columns, so it is "safe" to not check bounds

                    # Check top left
                    if str.isdigit(schematic[r-1][c-1]):
                        i = c - 2
                        while i >= 0 and str.isdigit(schematic[r - 1][i]):
                            i -= 1
                        # Found the end of the number, go back one
                        i += 1

                        numbers.append(get_number(schematic, r - 1, i))

                    # Left
                    if str.isdigit(schematic[r][c - 1]):
                        i = c - 2
                        while i >= 0 and str.isdigit(schematic[r][i]):
                            i -= 1
                        i += 1
                        numbers.append(get_number(schematic, r, i))

                    # Bottom left
                    if str.isdigit(schematic[r + 1][c - 1]):
                        i = c - 2
                        while i >= 0 and str.isdigit(schematic[r + 1][i]):
                            i -= 1
                        i += 1
                        numbers.append(get_number(schematic, r + 1, i))

                    # Top
                    if str.isdigit(schematic[r - 1][c]):
                        i = c - 1
                        while i >= 0 and str.isdigit(schematic[r - 1][i]):
                            i -= 1
                        i += 1
                        numbers.append(get_number(schematic, r - 1, i))

                    # Bottom
                    if str.isdigit(schematic[r + 1][c]):
                        i = c - 1
                        while i >= 0 and str.isdigit(schematic[r + 1][i]):
                            i -= 1
                        i += 1
                        numbers.append(get_number(schematic, r + 1, i))

                    # Top right
                    if str.isdigit(schematic[r - 1][c + 1]):
                        i = c
                        while i >= 0 and str.isdigit(schematic[r - 1][i]):
                            i -= 1
                        i += 1
                        numbers.append(get_number(schematic, r - 1, i))

                    # Right
                    if str.isdigit(schematic[r][c + 1]):
                        i = c
                        while i >= 0 and str.isdigit(schematic[r + 1][i]):
                            i -= 1
                        i += 1
                        numbers.append(get_number(schematic, r, i))

                    # Bottom right
                    if str.isdigit(schematic[r + 1][c + 1]):
                        i = c
                        while i >= 0 and str.isdigit(schematic[r + 1][i]):
                            i -= 1
                        i += 1
                        numbers.append(get_number(schematic, r + 1, i))

        print('--------------------------------------------------')
        print(numbers)
        print(*schematic, sep='\n')

        return sum([int(n) for n in numbers])

    def solve_part2(self):
        symbols = set('*')
        schematic = copy.deepcopy(self.parsed_input)
        gears = []

        print(*schematic, sep='\n')

        for r, row in enumerate(schematic):
            for c, val in enumerate(row):
                if val in symbols:
                    # Found symbol. Scan for numbers.
                    # Input does not have symbols in the border rows/columns, so it is "safe" to not check bounds

                    local_numbers = []

                    # Check top left
                    if str.isdigit(schematic[r - 1][c - 1]):
                        i = c - 2
                        while i >= 0 and str.isdigit(schematic[r - 1][i]):
                            i -= 1
                        # Found the end of the number, go back one
                        i += 1

                        local_numbers.append(get_number(schematic, r - 1, i))

                    # Left
                    if str.isdigit(schematic[r][c - 1]):
                        i = c - 2
                        while i >= 0 and str.isdigit(schematic[r][i]):
                            i -= 1
                        i += 1
                        local_numbers.append(get_number(schematic, r, i))

                    # Bottom left
                    if str.isdigit(schematic[r + 1][c - 1]):
                        i = c - 2
                        while i >= 0 and str.isdigit(schematic[r + 1][i]):
                            i -= 1
                        i += 1
                        local_numbers.append(get_number(schematic, r + 1, i))

                    # Top
                    if str.isdigit(schematic[r - 1][c]):
                        i = c - 1
                        while i >= 0 and str.isdigit(schematic[r - 1][i]):
                            i -= 1
                        i += 1
                        local_numbers.append(get_number(schematic, r - 1, i))

                    # Bottom
                    if str.isdigit(schematic[r + 1][c]):
                        i = c - 1
                        while i >= 0 and str.isdigit(schematic[r + 1][i]):
                            i -= 1
                        i += 1
                        local_numbers.append(get_number(schematic, r + 1, i))

                    # Top right
                    if str.isdigit(schematic[r - 1][c + 1]):
                        i = c
                        while i >= 0 and str.isdigit(schematic[r - 1][i]):
                            i -= 1
                        i += 1
                        local_numbers.append(get_number(schematic, r - 1, i))

                    # Right
                    if str.isdigit(schematic[r][c + 1]):
                        i = c
                        while i >= 0 and str.isdigit(schematic[r + 1][i]):
                            i -= 1
                        i += 1
                        local_numbers.append(get_number(schematic, r, i))

                    # Bottom right
                    if str.isdigit(schematic[r + 1][c + 1]):
                        i = c
                        while i >= 0 and str.isdigit(schematic[r + 1][i]):
                            i -= 1
                        i += 1
                        local_numbers.append(get_number(schematic, r + 1, i))

                    if len(local_numbers) == 2:
                        gears.append(int(local_numbers[0]) * int(local_numbers[1]))

        return sum(gears)



if __name__ == "__main__":
    solution = Day3Solution(day=3, example=None)
    # solution.run(part=1)
    solution.run(part=2)



