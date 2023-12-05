# https://adventofcode.com/2023/day/5

from solution import Solution


class Day5Solution(Solution):

    def parse_input(self):
        seeds = []
        maps = []

        for block in self.input_data.split('\n\n'):
            if block.startswith('seeds:'):
                seeds = [int(n) for n in block.split(':')[1].strip().split(' ')]
            else:
                m = []
                for line in block.split('\n'):
                    if line[0].isdigit():
                        m.append([int(n) for n in line.strip().split(' ')])
                maps.append(m)

        return [seeds, maps]

    def solve_part1(self):
        seeds = self.parsed_input[0]
        almanac = []

        for maps in self.parsed_input[1]:
            path = []
            for m in maps:
                path.append([range(m[1], m[1] + m[2]), m[0], m[1]])

            almanac.append(path)

        lookup = dict()
        for seed in seeds:
            for paths in almanac:
                start = seed
                for path in paths:
                    if seed in path[0]:
                        seed = path[1] + seed - path[2]
                        break
            lookup[start] = seed

        return lookup[min(lookup, key=lambda k: lookup[k])]

    def solve_part2(self):
        seed_ranges = [range(x, x + y) for x, y in list(zip(*[iter(self.parsed_input[0])] * 2))]
        almanac = [[[range(m[0], m[0] + m[2]), m[0], m[1]] for m in maps] for maps in self.parsed_input[1]]

        start_location = 1

        while True:
            # Backtrack through the maps from the location to the original seeds
            curser = len(almanac) - 1
            seed = start_location

            while curser >= 0:
                paths = almanac[curser]

                for path in paths:
                    if seed in path[0]:
                        seed = path[2] + seed - path[1]
                        break
                curser -= 1

            for path in seed_ranges:
                if seed in path:
                    # Found a path from a start location to an original seed. Break the loop and return
                    return start_location

            start_location += 1


if __name__ == "__main__":
    solution = Day5Solution(day=5, example=None)
    solution.run(part=1)
    solution.run(part=2)
