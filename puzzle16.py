from functools import wraps
from string import ascii_lowercase


def read_input():
    with open("puzzle16_input", "r") as f:
        return f.read().split(",")


def swap_by_index(i, j):
    @wraps(swap_by_index)
    def nested(line):
        line[j], line[i] = line[i], line[j]
        return line

    return nested


def swap_by_name(a, b):
    @wraps(swap_by_name)
    def nested(line):
        i, j = line.index(a), line.index(b)
        line[j], line[i] = line[i], line[j]
        return line

    return nested


def spin(i):
    @wraps(spin)
    def nested(line):
        first, last = line[:-i], line[-i:]
        line = last + first
        return line

    return nested


def parse_moves(raw_moves):
    res = []
    for mv in raw_moves:
        if mv[0] == "x":
            i, j = map(int, mv[1:].split("/"))
            res.append(swap_by_index(i, j))
            continue

        if mv[0] == "p":
            a, b = mv[1:].split("/")
            res.append(swap_by_name(a, b))
            continue

        if mv[0] == "s":
            split = int(mv[1:])
            res.append(spin(split))
    return res


def dance(line, moves, cycles=1):
    parsed_moves = parse_moves(moves)
    seen = []
    for i in xrange(cycles):
        saw = "".join(line)
        if saw in seen:
            return seen[cycles % i]
        seen.append(saw)
        for mv in parsed_moves:
            line = mv(line)

    return "".join(line)


def main():
    line = ascii_lowercase[:16]
    # assert dance([i for i in "abcde"], "s1,x3/4,pe/b".split(",")) == "baedc"
    # assert dance([i for i in "abcde"], "s1,x3/4,pe/b".split(","), 2) == "ceadb"

    # print(dance([i for i in line], read_input()))
    print(dance([i for i in line], read_input(), 1000000))


if __name__ == '__main__':
    main()
