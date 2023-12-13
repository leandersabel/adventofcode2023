# https://adventofcode.com/2023/day/13

from solution import Solution


class Day13Solution(Solution):

    def parse_input(self):
        return [pattern.split('\n') for pattern in self.input_data.split('\n\n')]

    def solve_part1(self):
        points = 0

        for pattern in self.parsed_input:
            horizontal = find_reflection(pattern)
            vertical = find_reflection([column for column in zip(*pattern)])
            points += vertical or (100 * horizontal)

        return points

    def solve_part2(self):
        points = 0

        for pattern in self.parsed_input:
            horizontal = find_reflection(pattern, 1)
            vertical = find_reflection([column for column in zip(*pattern)], 1)
            points += vertical or (100 * horizontal)

        return points


def find_reflection(pattern, smudges=0):
    for ln, line in enumerate(pattern[:-1]):
        i = ln
        j = ln + 1
        differences = 0

        while i >= 0 and j < len(pattern) and differences <= smudges:
            differences += sum(c1 != c2 for c1, c2 in zip(pattern[i], pattern[j]))
            i -= 1
            j += 1

        if differences == smudges:
            return ln + 1


if __name__ == "__main__":
    solution = Day13Solution(day=13, example=None)
    solution.run(part=1)
    solution.run(part=2)
