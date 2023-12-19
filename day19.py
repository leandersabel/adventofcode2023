# https://adventofcode.com/2023/day/19
import operator
import re
from collections import deque

import utils
from solution import Solution

operators = {'<': operator.lt, '>': operator.gt}
cat = {'x': 0, 'm': 1, 'a': 2, 's': 3}


class Day19Solution(Solution):

    def parse_input(self):
        block1, block2 = self.input_data.split('\n\n')

        workflows = dict()
        for line in block1.split('\n'):
            w_id = re.findall(r'(\w+){', line)[0]
            w_rules = re.findall(r'(\w)(\W)(\w+):(\w+)', line)
            rules = [[r[0], operators[r[1]], int(r[2]), r[3]] for r in w_rules]
            w_else = re.findall(r'(\w+)}', line)[0]
            workflows[w_id] = [rules, w_else]

        parts = []
        for line in block2.split('\n'):
            part_raw = re.findall(r'(\d+)', line)
            parts.append([int(val) for val in part_raw])

        return workflows, parts

    def solve_part1(self):
        workflows, parts = self.parsed_input
        stack = deque(['in', part] for part in parts)
        accepted = []

        while stack:
            wf_id, values = stack.pop()
            workflow = workflows.get(wf_id)
            else_target = workflow[1]

            for rule in workflow[0]:
                attribute, op, threshold, target = rule
                value = values[cat.get(attribute)]

                if op(value, threshold):
                    if target == 'A':
                        accepted.append(values)
                    elif target != 'R':
                        stack.append([target, values])
                    wf_id = None  # Stops processing of workflow else target
                    break

            if wf_id:  # Didn't find a match in the rules
                if else_target == 'A':
                    accepted.append(values)
                elif else_target != 'R':
                    stack.append([else_target, values])

        return sum(sum(values) for values in accepted)

    def solve_part2(self):
        pass


if __name__ == "__main__":
    solution = Day19Solution(day=19, example=None)
    solution.run(part=1)  # 280909
    # solution.run(part=2)
