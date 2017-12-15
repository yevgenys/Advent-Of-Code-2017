def read_input():
    with open("puzzle13_input", "r") as f:
        return f.read().splitlines()


def build_field(in_):
    tfield = {}
    field = []
    for i in in_:
        node, depth = map(lambda s: s.strip(), i.split(":"))
        tfield[node] = int(depth)

    max_ = int(in_[-1].split(":")[0])
    for i in range(max_ + 1):
        depth = tfield.get(str(i), 0)
        field.append((i, depth))

    return field


def calc_severity(firewalls):
    severity = 0
    for sec, depth in firewalls:
        if sec % (2 * (depth - 1)) == 0:
            severity += depth * sec
    return severity


def calc_delay(firewalls, delay=0):
    while True:
        for sec, depth in firewalls:
            if depth == 0:
                continue

            if (sec + delay) % (2 * (depth - 1)) == 0:
                delay += 1
                break
        else:
            break
    return delay


if __name__ == '__main__':
    test_in = """0: 3
1: 2
4: 4
6: 4"""

    test_field = build_field(test_in.splitlines())
    assert calc_severity(test_field) == 24
    assert calc_delay(test_field) == 10

    field = build_field(read_input())
    print(calc_severity(field))
    print(calc_delay(field))
