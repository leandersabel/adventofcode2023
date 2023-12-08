# https://adventofcode.com/2023/day/8
import math
import re
from itertools import cycle

from solution import Solution

direction = {'L': 0, 'R': 1}


class Day8Solution(Solution):

    def parse_input(self):
        instructions, network = self.input_data.split('\n\n')[:2]
        network = [list(re.findall(r'(\w+) = \((\w+), (\w+)\)', n))[0] for n in network.split('\n')]
        network = {l[0]: [l[1], l[2]] for l in network}
        return [instructions, network]

    def solve_part1(self):
        instructions = self.parsed_input[0]
        network = self.parsed_input[1]

        node = 'AAA'
        path = []

        for instruction in cycle(instructions):
            node = network.get(node)[direction[instruction]]
            path.append(node)
            if node == 'ZZZ': break

        return len(path)

    def solve_part2(self):
        instructions = self.parsed_input[0]
        network = self.parsed_input[1]

        nodes = [node for node in network.keys() if node[2] == 'A']
        paths = [[] for _ in range(len(nodes))]

        for n in range(len(nodes)):
            for instruction in cycle(instructions):
                nodes[n] = network.get(nodes[n])[direction[instruction]]
                paths[n].append(nodes[n])
                if nodes[n][2] == 'Z': break

        return math.lcm(*[len(path) for path in paths])


if __name__ == "__main__":
    solution = Day8Solution(day=8, example=None)
    solution.run(part=1)
    solution.run(part=2)
