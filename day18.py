# https://adventofcode.com/2023/day/18
from shapely.ops import unary_union

from solution import Solution
from shapely.geometry import Point, Polygon, MultiPolygon

directions = {'R': [1, 0], 'L': [-1, 0], 'U': [0, -1], 'D': [0, 1]}
hex_dirs = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}


class Day18Solution(Solution):

    def parse_input(self):
        return [line.split(' ') for line in self.input_data.split('\n')]

    def solve_part1(self):
        digger = Point(0, 0)
        trenches = []

        for instruction in self.parsed_input:
            direction, length, color = instruction
            dx, dy = directions.get(direction)
            lx, ly = dx * int(length), dy * int(length)

            trench, digger = dig(digger, direction, lx, ly)
            trenches.append(trench)

        return calculate_exterior_area(trenches)

    def solve_part2(self):
        digger = Point(0, 0)
        trenches = []

        for instruction in self.parsed_input:
            direction = hex_dirs.get(instruction[2][-2])
            dx, dy = directions.get(direction)
            length = int(instruction[2][2:7], 16)
            lx, ly = dx * int(length), dy * int(length)

            trench, digger = dig(digger, direction, lx, ly)
            trenches.append(trench)

        return calculate_exterior_area(trenches)


def dig(digger, direction, lx, ly):
    """
    Create a polygon for the area dug out by moving the digger from its current location into the given direction.
    :param digger: Current digger location
    :type digger: Point
    :param direction: 'R'(ight), 'L'(eft), 'U'(p), or 'D'(own)
    :type direction: string
    :param lx: Length to move along the x-axis
    :type lx: int
    :param ly: Length to move along the y-axis
    :type ly: int
    :return: Tuple of the polygon representing trench, and the new digger location
    :rtype:  list[Polygon, Point]
    """
    if direction == 'L' or direction == 'U':
        digger = Point(digger.x + lx, digger.y + ly)

    # Calculate the coordinates of the four corners of the large box
    ll = Point(digger.x, digger.y)
    lr = (ll.x + abs(lx) + 1, ll.y)
    ul = (ll.x, ll.y + abs(ly) + 1)
    ur = (ll.x + abs(lx) + 1, ll.y + abs(ly) + 1)

    trench = Polygon([ll, lr, ur, ul])

    if direction == 'R' or direction == 'D':
        digger = Point(digger.x + lx, digger.y + ly)

    return [trench, digger]


def calculate_exterior_area(trenches):
    """
    Merge the polygons, extract the exterior, and compute the area.
    :param trenches: A list of polygons representing the trenches, forming a closed loop
    :type trenches: list[Polygon]
    :return: The area of the merged polygon
    """
    merged_polygon = unary_union(MultiPolygon(trenches))
    exterior_polygon = Polygon(merged_polygon.exterior)
    return int(exterior_polygon.area)


if __name__ == "__main__":
    solution = Day18Solution(day=18, example=None)
    solution.run(part=1)
    solution.run(part=2)
