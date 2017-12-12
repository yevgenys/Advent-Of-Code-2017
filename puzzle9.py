from aetypes import Enum


def read_input():
    with open("puzzle9_input", "r") as f:
        return f.read()


class StateMap(Enum):
    idle, garbage, group, ignore_next = range(4)


STATE_MAP = {
    "<": StateMap.garbage,
    "{": StateMap.group,
    "!": StateMap.ignore_next,
    ",": StateMap.idle
}


class State(object):
    def __init__(self, prev_state, cur_state):
        self.prev_state = prev_state
        self.cur_state = cur_state


def next_state(char, state, count_groups, depth, score, garbage_counter):
    new_state = state
    if state.cur_state is StateMap.garbage:
        if char == ">":
            new_state = State(state.prev_state, state.prev_state.cur_state)
        elif char == "!":
            new_state = State(state, StateMap.ignore_next)
        else:
            garbage_counter += 1

    if state.cur_state is StateMap.group:
        if char == "<":
            new_state = State(state, StateMap.garbage)
        if char == "!":
            new_state = State(state, StateMap.ignore_next)
        if char == "}":
            new_state = State(state, state.prev_state.cur_state)
            count_groups += 1
            score += 1 + depth
            depth -= 1
        if char == "{":
            depth += 1
            new_state = State(state, StateMap.group)

    if state.cur_state is StateMap.ignore_next:
        new_state = State(state.prev_state.prev_state, state.prev_state.cur_state)

    if state.cur_state is StateMap.idle:
        depth = 0
        new_state = State(state, STATE_MAP[char])

    return new_state, count_groups, depth, score, garbage_counter


def count_score(stream):
    state = State(State(None, StateMap.idle), STATE_MAP[stream[0]])
    garbage_counter = depth = score = groups = 0
    for char in stream[1:]:
        state, groups, depth, score, garbage_counter = next_state(char, state, groups, depth, score, garbage_counter)
    return score, groups, garbage_counter


if __name__ == '__main__':
    test_in = '<>,<random characters>,<<<<>,<{!>}>,<!!>,<!!!>>,<{o"i!a,<{i<a>,{},{{{}}},{{},{}},{{{},{},{{}}}},{<{},{},{{}}>},{<a>,<a>,<a>,<a>},{{<a>},{<a>},{<a>},{<a>}},{{<!>},{<!>},{<!>},{<a>}}'
    res = count_score(test_in)
    assert res[1] == 22

    test_in2 = '{},{{{}}},{{},{}},{{{},{},{{}}}},{<a>,<a>,<a>,<a>},{{<ab>},{<ab>},{<ab>},{<ab>}},{{<!!>},{<!!>},{<!!>},{<!!>}},{{<a!>},{<a!>},{<a!>},{<ab>}}'
    assert count_score(test_in2)[1] == 26
    assert count_score(test_in2)[0] == 50

    print(count_score(read_input()))
