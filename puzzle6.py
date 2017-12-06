def count_cycles_till_infinite_loop(banks):
    prev_states = []
    cycles = 0
    while True:
        prev_states.append(banks[:])
        max_el_index = banks.index(max(banks))
        redistribute(max_el_index, banks)
        cycles += 1
        if banks in prev_states:
            prev_states.append(banks[:])
            return cycles, prev_states


def redistribute(index, lst):
    spread_value = lst[index]
    lst[index] = 0
    index += 1
    length = len(lst)
    if spread_value > length:
        lst.append(0)
        length = len(lst)
    while True:
        if spread_value <= 0:
            break
        lst[index % length] += 1
        index += 1
        spread_value -= 1


def count_distance_from_last_element_till_its_copy(lst):
    start_element = lst.pop(len(lst) - 1)
    distance = 0
    for el in lst[::-1]:
        distance += 1
        if start_element == el:
            break
    return distance


if __name__ == '__main__':
    steps, states = count_cycles_till_infinite_loop([0, 2, 7])
    assert steps == 5
    assert count_distance_from_last_element_till_its_copy(states) == 4

    steps, all_states = count_cycles_till_infinite_loop([14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4])
    print(steps)
    print(count_distance_from_last_element_till_its_copy(all_states))
