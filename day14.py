# https://adventofcode.com/2023/day/14
import copy

from solution import Solution


class Day14Solution(Solution):

    def parse_input(self):
        return [list(row) for row in self.input_data.split('\n')]

    def solve_part1(self):
        platform_t = [list(col) for col in zip(*self.parsed_input)]
        platform_t = shift_left(platform_t)
        platform = [list(col) for col in zip(*platform_t)]
        return sum([(len(platform) - r) * row.count('O') for r, row in enumerate(platform)])

    def solve_part2(self):
        platform_t = [list(col) for col in zip(*self.parsed_input)]
        history = []

        while platform_t not in history:
            history.append(copy.deepcopy(platform_t))
            for _ in range(4):
                platform_t = shift_left(platform_t)
                platform_t = rotate_matrix(platform_t)

        first_match = history.index(platform_t)
        second_match = len(history)

        final_conf = first_match + (1000000000 - first_match) % (second_match - first_match)
        platform_t = history[final_conf]
        platform = [list(col) for col in zip(*platform_t)]
        return sum([(len(platform) - r) * row.count('O') for r, row in enumerate(platform)])


def shift_left(platform):
    for col in platform:
        last_free = 0 if col[0] == '.' else None
        c = 0
        while c < len(col):
            if col[c] == '.' and last_free is None:
                last_free = c
            elif col[c] == '#':
                last_free = None
            elif col[c] == 'O' and last_free is not None:
                col[last_free], col[c] = 'O', '.'
                c, last_free = last_free, None
            c += 1
    return platform


def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1, -1, -1)]


if __name__ == "__main__":
    solution = Day14Solution(day=14, example=None)
    solution.run(part=1)
    solution.run(part=2)
