from collections import namedtuple

from itertools import cycle

Point = namedtuple("Point", ["x", "y"])
Node = namedtuple("Node", ["value", "point"])


def right(point):
    return Point(point.x + 1, point.y)


def left(point):
    return Point(point.x - 1, point.y)


def up(point):
    return Point(point.x, point.y + 1)


def down(point):
    return Point(point.x, point.y - 1)


def build_spiral_matrix(max_value):
    position = Point(0, 0)
    node = Node(1, position)
    moves = cycle([right, up, left, down])
    matrix = [node]
    row_length = 1

    while True:
        for _ in xrange(2):
            next_move = next(moves)
            for _ in xrange(row_length):
                if node.value > max_value:
                    return matrix
                next_point = next_move(node.point)
                node = Node(calc_node_value(next_point, matrix), next_point)
                matrix.append(node)
        row_length += 1


def calc_node_value(start_point, matrix):
    possible_neighbors_coordinates = neighbor_coordinates(start_point)
    neighbor_nodes = []
    for i, search_node in enumerate(matrix[::-1]):
        if search_node.point in possible_neighbors_coordinates:
            neighbor_nodes.append(search_node)
        if len(neighbor_nodes) >= 4:
            break
    return sum(map(lambda n: n.value, neighbor_nodes))


def neighbor_coordinates(point):
    return map(lambda m: m(point), [
        left,
        down,
        right,
        up,
        lambda p: up(left(p)),
        lambda p: up(right(p)),
        lambda p: down(right(p)),
        lambda p: down(left(p)),
    ])


def calc_steps_to_beginning(point):
    return abs(point.x) + abs(point.y)


def get_coordinates(max_value):
    position = Point(0, 0)
    val = 1
    moves = cycle([right, up, left, down])
    row_length = 1

    while True:
        for _ in xrange(2):
            next_move = next(moves)
            for _ in xrange(row_length):
                if val >= max_value:
                    return position
                position = next_move(position)
                val += 1
        row_length += 1


if __name__ == '__main__':
    print(calc_steps_to_beginning(get_coordinates(312051)))  # part1

    # part2
    matrix = build_spiral_matrix(312051)
    print(matrix[-1])

