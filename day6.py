# https://adventofcode.com/2023/day/6

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

        approach = 'binary-search'  # Options are 'naive' or 'binary-search'

        if approach == 'naive':
            for t in range(0, time + 1):
                if predict(t, time) > distance:
                    first_win = t
                    break

        elif approach == 'binary-search':
            c = math.ceil(time / 2)
            window = [0, time]

            while first_win is None:
                result = predict(c, time)

                if window[1] - window[0] == 0:
                    first_win = c + 1

                if result > distance:
                    window = [window[0], c - 1]
                    c = window[1] - math.ceil((window[1] - window[0]) / 2)
                else:
                    window = [c + 1, window[1]]
                    c = window[0] + math.ceil((window[1] - window[0]) / 2)

        return time - 1 - (first_win - 1) * 2


def predict(hold_time, race_time):
    return (race_time - hold_time) * hold_time


if __name__ == "__main__":
    solution = DaySolution(day=6, example=None)
    solution.run(part=1)
    solution.run(part=2)
