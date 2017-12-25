import re

import sys


def read_input():
    with open("puzzle20_input", "r") as f:
        return f.read().splitlines()


SPLITTER = re.compile("p=<(?P<pos>[-0-9,]+)>,\sv=<(?P<vel>[-0-9,]+)>,\sa=<(?P<acc>[-0-9,]+)>")


class Particle:
    def __init__(self, index, pos, vel, acc):
        self.index = index
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def next_pos(self):
        self.vel = [a + b for a, b in zip(self.vel, self.acc)]
        self.pos = [a + b for a, b in zip(self.vel, self.pos)]

    @property
    def manhattan_distance(self):
        return sum(map(abs, self.pos))

    def __lt__(self, other):
        return other.manhattan_distance > self.manhattan_distance

    def show(self):
        print(
            "Particle<{}>(Position: {}; Velocity: {}; Acceleration: {})".format(self.index, self.pos, self.vel,
                                                                                self.acc))


def _to_int(str_):
    return map(int, str_.split(","))


def parse_(particles):
    res = []
    for i, p in enumerate(particles):
        m = SPLITTER.match(p)
        group = m.group("pos")
        res.append(Particle(i, _to_int(group), _to_int(m.group("vel")), _to_int(m.group("acc"))))
    return res


def get_closest_index(parsed_particles):
    min_ = parsed_particles[0]
    for p in parsed_particles:
        if p < min_:
            min_ = p
    return min_


def run_p1(particles):
    parsed_particles = parse_(particles)
    for _ in xrange(500):
        map(lambda p: p.next_pos(), parsed_particles)

    return get_closest_index(parsed_particles)


def remove_all_dups(dups, parsed_particles):
    new_val = parsed_particles
    while len(dups):
        dup = dups.pop()
        new_val = filter(lambda p: p.pos != dup, new_val)
    return new_val


def get_dup_distances(parsed_particles):
    seen = []
    dups = []
    for part in parsed_particles:
        if part.pos in seen and part.pos not in dups:
            dups.append(part.pos)
        seen.append(part.pos)
    return dups


def run_p2(particles):
    parsed_particles = parse_(particles)
    for i in xrange(100):
        map(lambda p: p.next_pos(), parsed_particles)
        dups = get_dup_distances(parsed_particles)
        parsed_particles = remove_all_dups(dups, parsed_particles)

    return parsed_particles


if __name__ == '__main__':
    test_in = """p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>""".splitlines()
    assert run_p1(test_in).index == 0

    run_p1(read_input()).show()

    test_in2 = """p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>    
p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>""".splitlines()

    assert len(run_p2(test_in2)) == 1

    print("Part2: %d" % len(run_p2(read_input())))
