# https://adventofcode.com/2023/day/16
from collections import deque

from solution import Solution

directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
tiles = {'.': {'R': ['R'], 'L': ['L'], 'U': ['U'], 'D': ['D']},
         '/': {'R': ['U'], 'L': ['D'], 'U': ['R'], 'D': ['L']},
         '⟍': {'R': ['D'], 'L': ['U'], 'U': ['L'], 'D': ['R']},
         '-': {'R': ['R'], 'L': ['L'], 'U': ['L', 'R'], 'D': ['L', 'R']},
         '|': {'R': ['U', 'D'], 'L': ['U', 'D'], 'U': ['U'], 'D': ['D']}}


class Day16Solution(Solution):

    def parse_input(self):
        return [[char if char != '\\' else '⟍' for char in line] for line in self.input_data.split('\n')]

    def solve_part1(self):
        contraption = self.parsed_input
        return process_beam(contraption, [[(0, 0), 'R']])

    def solve_part2(self):
        contraption = self.parsed_input

        max_rows, max_cols = len(contraption), len(contraption[0])
        starting_positions = ([[(r, 0), 'R'] for r in range(max_rows)] +
                              [[(r, max_cols - 1), 'L'] for r in range(max_rows)] +
                              [[(0, c), 'D'] for c in range(max_cols)] +
                              [[(max_rows - 1, c), 'U'] for c in range(max_cols)])
        starting_positions = [[pos] for pos in starting_positions]

        all_path = []
        for starting_position in starting_positions:
            all_path.append(process_beam(contraption, starting_position))

        return max(all_path)


def process_beam(contraption, start):
    beams = deque(start)
    visited = set()
    loop_breaker = set()

    while beams:
        beam = beams.pop()
        row, col = beam[0]
        current_direction = beam[1]
        visited.add((row, col))

        if (row, col, current_direction) in loop_breaker:
            continue  # Processed this tile and this direction before -> Skip

        loop_breaker.add((row, col, current_direction))
        new_directions = tiles.get(contraption[row][col]).get(current_direction)

        for direction in new_directions:
            dr, dc = directions.get(direction)
            if 0 <= row + dr < len(contraption) and 0 <= col + dc < len(contraption[0]):
                beams.append([(row + dr, col + dc), direction])

    return len(visited)


if __name__ == "__main__":
    solution = Day16Solution(day=16, example=None)
    solution.run(part=1)
    solution.run(part=2)
