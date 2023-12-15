# https://adventofcode.com/2023/day/15
import re
from functools import reduce

import utils
from solution import Solution


class Day15Solution(Solution):

    def parse_input(self):
        return self.input_data.split(',')

    def solve_part1(self):
        return sum([hash_aoc15(seq) for seq in self.parsed_input])

    def solve_part2(self):
        boxes = {i: [] for i in range(256)}
        for seq in self.parsed_input:
            insert = '=' in seq
            label, focal = re.split(r'[-=]', seq)
            box_id = hash_aoc15(label)
            index = next((p for p, pair in enumerate(boxes[box_id]) if label == pair[0]), None)

            if insert:
                utils.replace_or_append(boxes[box_id], index, [label, focal])
            elif index is not None:  # Remove
                boxes[box_id].pop(index)

        return sum([(b + 1) * (l + 1) * int(lens[1]) for b, box in boxes.items() for l, lens in enumerate(box)])


def hash_aoc15(string):
    return reduce(lambda value, c: ((value + ord(c)) * 17) % 256, string, 0)


if __name__ == "__main__":
    solution = Day15Solution(day=15, example=None)
    solution.run(part=1)
    solution.run(part=2)
