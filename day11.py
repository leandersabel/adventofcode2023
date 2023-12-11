# https://adventofcode.com/2023/day/11
import copy

import utils
from solution import Solution


class Day11Solution(Solution):

    def parse_input(self):
        image = [list(col) for col in self.input_data.split('\n')]
        empty_rows = [r for r, row in enumerate(image) if '#' not in row]
        empty_cols = [c for c, col in enumerate(zip(*image)) if '#' not in col]

        return [image, [empty_rows, empty_cols]]

    def solve_part1(self):
        image = copy.deepcopy(self.parsed_input[0])
        empty_rows, empty_cols = self.parsed_input[1]

        # Add empty rows
        for r, row in enumerate(empty_rows):
            image.insert(row + r, list('.' * len(image[0])))

        # Add empty columns (on transposed list for easier list handling)
        t_image = [list(column) for column in zip(*image)]
        for c, col in enumerate(empty_cols):
            t_image.insert(col + c, list('.' * len(t_image[0])))
        expansion = [list(col) for col in zip(*t_image)]

        galaxies = [[r, c] for r, row in enumerate(expansion) for c, col in enumerate(row) if col == '#']
        galaxy_pairs = [(a, b) for i, a in enumerate(galaxies) for b in galaxies[i + 1:]]
        return sum(utils.manhattan_distance(pair[0], pair[1]) for pair in galaxy_pairs)

    def solve_part2(self):
        image = self.parsed_input[0]
        empty_rows, empty_cols = self.parsed_input[1]
        galaxies = [[r, c] for r, row in enumerate(image) for c, col in enumerate(row) if col == '#']

        # Make each empty row or column one million times larger
        exp = 1000000 - 1

        for r, row in enumerate(empty_rows):
            for galaxy in galaxies:
                if galaxy[0] > row + r * exp:
                    galaxy[0] += exp

        for c, col in enumerate(empty_cols):
            for galaxy in galaxies:
                if galaxy[1] > col + c * exp:
                    galaxy[1] += exp

        galaxy_pairs = [(a, b) for i, a in enumerate(galaxies) for b in galaxies[i + 1:]]

        return sum(utils.manhattan_distance(pair[0], pair[1]) for pair in galaxy_pairs)


if __name__ == "__main__":
    solution = Day11Solution(day=11, example=None)
    solution.run(part=1)
    solution.run(part=2)
