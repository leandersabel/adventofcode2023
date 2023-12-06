# https://adventofcode.com/2023/day/

import math

from solution import Solution


class DaySolution(Solution):

    def parse_input(self):
        data = self.input_data.split('\n')
        time = data[0].split(':')[1].strip().split()
        distance = data[1].split(':')[1].strip().split()
        return [time, distance]

    def solve_part1(self):
        time = [int(t) for t in self.parsed_input[0]]
        distance = [int(d) for d in self.parsed_input[1]]
        wins = [0] * len(time)

        for i in range(len(time)):
            for t in range(0, time[i] + 1):
                if predict(t, time[i]) > distance[i]:
                    wins[i] += 1

        return math.prod(wins)

    def solve_part2(self):
        time = int(''.join([t for t in self.parsed_input[0]]))
        distance = int(''.join([d for d in self.parsed_input[1]]))
        first_win = None

        for t in range(0, time + 1):
            if predict(t, time) > distance:
                first_win = t
                break

        return time - 1 - (first_win - 1) * 2


def predict(hold_time, race_time):
    return (race_time - hold_time) * hold_time


if __name__ == "__main__":
    solution = DaySolution(day=6, example=None)
    solution.run(part=1)
    solution.run(part=2)
