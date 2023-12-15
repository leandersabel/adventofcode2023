# https://adventofcode.com/2023/day/12
import re

from solution import Solution


class Day12Solution(Solution):

    def parse_input(self):
        return [line.split(' ') for line in self.input_data.split('\n')]

    def solve_part1(self):

        arrangement = []

        for line in self.parsed_input:
            springs, groups = line

            pattern = r'^\.*'
            for val in groups.split(','):
                pattern += r'#{' + val + r'}\.+'
            pattern = pattern[:-3] + r'\.*$'

            arrangement.extend([string for string in generate_permutations(springs) if re.findall(pattern, string)])

        return len(arrangement)


    def solve_part2(self):
        pass


def generate_permutations(s, index=0, current=''):
    permutations = []

    if index == len(s):
        permutations.append(current)
        return permutations

    if s[index] == '?':
        permutations += generate_permutations(s, index + 1, current + '.')
        permutations += generate_permutations(s, index + 1, current + '#')
    else:
        permutations += generate_permutations(s, index + 1, current + s[index])

    return permutations




if __name__ == "__main__":
    solution = Day12Solution(day=12, example=None)
    solution.run(part=1)
    #solution.run(part=2)
