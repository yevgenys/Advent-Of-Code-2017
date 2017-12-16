def knot_hash(lengths, rounds=1, range_=None):
    cur_pos = skip_size = 0
    lst = range_ if range_ else range(256)
    lengths += [17, 31, 73, 47, 23]
    for round in xrange(rounds):
        for length in lengths:
            sublist = []
            indexs = []
            for i in xrange(length):
                indexs.append((cur_pos + i) % len(lst))
                sublist.append(lst[indexs[i]])
            sublist.reverse()
            for i, parent_index in enumerate(indexs):
                lst[parent_index] = sublist[i]
            cur_pos = cur_pos + (skip_size + length)
            skip_size += 1
    return lst


def sparse_hash(lst):
    return [reduce(lambda a, b: a ^ b, chunck) for chunck in chunks(lst)]


def chunks(l):
    for i in range(0, len(l), 16):
        yield l[i:i + 16]


def create_single_hash_from_sparse_hashs(hex_):
    return "".join(map(lambda d: "0" + d if len(d) == 1 else d, map(lambda h: h[2:], hex_)))


if __name__ == '__main__':
    hash = knot_hash([165, 1, 255, 31, 87, 52, 24, 113, 0, 91, 148, 254, 158, 2, 73, 153])
    print(hash[0] * hash[1])

    test1 = knot_hash(map(ord, "1,2,3"), 64)
    test1_res = create_single_hash_from_sparse_hashs(map(hex, sparse_hash(test1)))
    assert test1_res == "3efbe78a8d82f29979031a4aa0b16a9d"

    arr = map(ord, "165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153")
    answ = knot_hash(arr, 64)
    print(create_single_hash_from_sparse_hashs(map(hex, sparse_hash(answ))))
