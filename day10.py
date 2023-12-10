# https://adventofcode.com/2023/day/10
import math
from collections import deque

import utils
from solution import Solution

pipe = {'|': ['N', 'S'], '-': ['E', 'W'], 'L': ['E', 'N'], 'J': ['N', 'W'], '7': ['S', 'W'], 'F': ['E', 'S'],
        'S': ['E', 'N', 'S', 'W']}
connection = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
directions = {'N': [-1, 0], 'S': [1, 0], 'W': [0, -1], 'E': [0, 1]}


class Day10Solution(Solution):

    def parse_input(self):
        grid = self.input_data.split('\n')
        start = [[r, c] for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 'S'][0]
        graph = [[pipe.get(col, []) for col in row] for row in grid]
        return [graph, grid, start]

    def solve_part1(self):
        graph = self.parsed_input[0]
        queue = deque([self.parsed_input[2]])
        visited = []

        # Run breadth first search
        while queue:
            visited.append(queue.popleft())
            queue.extend([neighbor for neighbor in get_neighbors(graph, visited[-1]) if neighbor not in visited])

        return math.floor(len(visited) / 2)

    def solve_part2(self):
        graph = self.parsed_input[0]
        grid = [list(node) for node in self.parsed_input[1]]
        start = self.parsed_input[2]

        grid[start[0]][start[1]] = get_start_shape(graph, start)
        queue = deque([start])
        visited = []

        # Run breadth first search
        while queue:
            visited.append(queue.popleft())
            queue.extend([neighbor for neighbor in get_neighbors(graph, visited[-1]) if neighbor not in visited])

        # Replace all pipes that are not part of the loop with '.'
        grid = [['.' if [r, c] not in visited else col for c, col in enumerate(row)] for r, row in enumerate(grid)]

        # Do the thing.
        count = 0
        for r, row in enumerate(grid):
            inside = False
            last_bend = ''

            for c, col in enumerate(row):
                if col in ['F', 'L']:
                    last_bend = col
                elif col == '|' or col == 'J' and last_bend == 'F' or col == '7' and last_bend == 'L':
                    inside = not inside
                elif col == '.' and inside:
                    count += 1

        return count


def get_neighbors(graph, node):
    r, c = node
    neighbors = []

    for pc in graph[r][c]:
        dr, dc = directions.get(pc)
        if 0 <= r + dr < len(graph) and 0 <= c + dc < len(graph[r]):
            if pc in [connection.get(con) for con in graph[r + dr][c + dc]]:
                neighbors.append([r + dr, c + dc])

    return neighbors


def get_start_shape(graph, start):
    dr = [[sn[0] - start[0], sn[1] - start[1]] for sn in get_neighbors(graph, start)]
    direction = utils.get_keys_by_value(directions, dr)
    shape = utils.get_key_by_value(pipe, direction)
    return shape


if __name__ == "__main__":
    solution = Day10Solution(day=10, example=None)
    solution.run(part=1)
    solution.run(part=2)
