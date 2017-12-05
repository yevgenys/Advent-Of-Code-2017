def read_input():
    with open("./puzzle5_input", 'r') as f:
        return f.read()


def count_jumps_with_inc_elements(lst):
    steps = 0
    next_step = 0
    while True:
        if next_step > len(lst) - 1:
            return steps
        value = lst[next_step]
        lst[next_step] += 1
        next_step = next_step + value
        steps += 1


def count_jumps_with_inc_dec_elements(lst):
    steps = 0
    next_step = 0
    while True:
        if next_step > len(lst) - 1:
            return steps
        value = lst[next_step]
        lst[next_step] = value + 1 if value < 3 else value - 1
        next_step = next_step + value
        steps += 1


if __name__ == '__main__':
    in_ = read_input()
    assert count_jumps_with_inc_elements([0, 3, 0, 1, -3]), 5
    assert count_jumps_with_inc_dec_elements([0, 3, 0, 1, -3]), 10

    print(count_jumps_with_inc_elements(map(int, in_.splitlines())))
    print(count_jumps_with_inc_dec_elements(map(int, in_.splitlines())))
