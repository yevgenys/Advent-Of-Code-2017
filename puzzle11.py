def read_input():
    with open("puzzle11_input", "r") as f:
        return f.read().split(",")


def right(x, y):
    return x + 1, y


def left(x, y):
    return x - 1, y


def up(x, y):
    return x, y + 1


def down(x, y):
    return x, y - 1


STEPS = {
    "n": lambda x, y: (x, y + 2),
    "s": lambda x, y: (x, y - 2),
    "w": lambda x, y: (x - 2, y),
    "e": lambda x, y: (x + 2, y),
    "ne": lambda x, y: (x + 1, y + 1),
    "nw": lambda x, y: (x - 1, y + 1),
    "sw": lambda x, y: (x - 1, y - 1),
    "se": lambda x, y: (x + 1, y - 1)
}


def count_final_distance(directions):
    x = y = 0
    max_distance = 0
    for direction in directions:
        x, y = STEPS.get(direction)(x, y)
        distance = count_distance(x, y)
        if distance > max_distance:
            max_distance = distance
    return count_distance(x, y), max_distance


def count_distance(x, y):
    return (abs(x) + abs(y)) / 2


if __name__ == '__main__':
    test_in_1 = "ne,ne,ne"
    assert count_final_distance(test_in_1.split(","))[0] == 3

    test_in_2 = "ne,ne,sw,sw"
    assert count_final_distance(test_in_2.split(","))[0] == 0

    test_in_3 = "ne,ne,s,s"
    assert count_final_distance(test_in_3.split(","))[0] == 2

    test_in_4 = "se,sw,se,sw,sw"
    assert count_final_distance(test_in_4.split(","))[0] == 3

    print(count_final_distance(read_input()))
