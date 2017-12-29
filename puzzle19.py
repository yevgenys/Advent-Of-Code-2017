D_MAP = {
    "D": lambda i, j: (i + 1, j),
    "U": lambda i, j: (i - 1, j),
    "L": lambda i, j: (i, j - 1),
    "R": lambda i, j: (i, j + 1)
}

OPPOSITE = {
    "D": "U",
    "U": "D",
    "L": "R",
    "R": "L"
}


def read_input():
    with open("puzzle19_input", "r") as f:
        return f.read().splitlines()


def find_start(in_):
    for i, el in enumerate(in_):
        if el == "|":
            return 0, i


def find_next_direction(direction, next_, in_, i, j):
    if next_ == "+":
        for d in filter(lambda d: d != OPPOSITE[direction], "DULR"):
            n_i, n_j = D_MAP[d](i, j)
            if len(in_) > n_i and in_[n_i][n_j] != " ":
                return d

    return direction


def walk(in_):
    i, j = find_start(in_[0])
    direction = "D"
    res = []
    steps = 1
    while direction:
        i, j = D_MAP[direction](i, j)
        next_ = in_[i][j]
        if next_ == " ":
            break
        elif next_ not in "+-|":
            res.append(next_)
        else:
            direction = find_next_direction(direction, next_, in_, i, j)
        steps += 1

    return "".join(res), steps


if __name__ == '__main__':
    test_in = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+""".splitlines()

    assert walk(test_in)[0] == "ABCDEF"
    assert walk(test_in)[1] == 38

    print(walk(read_input()))
