def spin(steps, seek=2017):
    cur_pos = 0
    res = [0]

    for i in xrange(seek):
        cur_pos = ((cur_pos + steps) % len(res)) + 1
        res.insert(cur_pos, i + 1)
    return res


def spin_part2(steps, cycles=50000000):
    cur_pos = 0
    res = 0

    for i in xrange(cycles):
        cur_pos = ((cur_pos + steps) % (i+1)) + 1
        if cur_pos == 1:
            res = i
    return res + 1


if __name__ == '__main__':
    res = spin(324, 2017)
    print "Part1: {}".format(res[1])
    print "Part2: {}".format(spin_part2(324))
