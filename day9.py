# https://adventofcode.com/2023/day/9

from solution import Solution


class Day9Solution(Solution):

    def parse_input(self):
        # Original report of history data from OASIS
        report = [[int(val) for val in line.split(' ')] for line in self.input_data.split('\n')]

        # Initialize list of lists of differences with first rows
        diffs = [[[history[i + 1] - history[i] for i in range(len(history) - 1)]] for history in report]

        for h, history in enumerate(report):
            # Reduce list of differences until all values are 0
            while any(val != 0 for val in diffs[h][-1]):
                diffs[h].append([diffs[h][-1][i + 1] - diffs[h][-1][i] for i in range(len(diffs[h][-1]) - 1)])

        return [report, diffs]

    def solve_part1(self):
        report = self.parsed_input[0]
        diffs = self.parsed_input[1]

        for d, dif in enumerate(diffs):
            # Extrapolate predictions from the bottom up
            report[d].append(report[d][-1] + sum(dif[i - 1][-1] for i in range(len(dif), 0, -1)))

        return sum([r[-1] for r in report])

    def solve_part2(self):
        report = self.parsed_input[0]
        diffs = self.parsed_input[1]

        for d, dif in enumerate(diffs):
            # Extrapolate predictions from the bottom up
            prediction = 0
            for i in range(len(dif), 0, -1):
                prediction = dif[i - 1][0] - prediction
            report[d].insert(0, report[d][0] - prediction)

        return sum([r[0] for r in report])


if __name__ == "__main__":
    solution = Day9Solution(day=9, example=None)
    solution.run(part=1)
    solution.run(part=2)
