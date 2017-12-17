import sys

A_FACTOR = 16807
B_FACTOR = 48271
PRODUCT = 2147483647

def to_bin(int_val):
    return bin(int_val)[2:]

def get_tail(bin_val):
    return bin_val[-16:]

def generate_next(seed, factor):
    return (seed * factor) % PRODUCT

def count_total_similarities_in_16_bits_part1(a, b, cycles):
    total = 0
    for i in xrange(cycles + 1):
        if get_tail(to_bin(a)) == get_tail(to_bin(b)):
            total += 1
        a, b = generate_next(a, A_FACTOR), generate_next(b, B_FACTOR)

    return total

def generate_next_p2(seed, factor, multiples):
    while True:
        seed = res = (seed * factor) % PRODUCT
        if (res % multiples) == 0:
            return res

def count_total_similarities_in_16_bits_part2(a, b, cycles):
    total = 0
    for i in xrange(cycles + 1):
        if get_tail(to_bin(a)) == get_tail(to_bin(b)):
            total += 1
        a = generate_next_p2(a, A_FACTOR, 4)
        b = generate_next_p2(b, B_FACTOR, 8)

    return total

def main():
    assert count_total_similarities_in_16_bits_part1(65, 8921, 5) == 1
    assert count_total_similarities_in_16_bits_part2(65, 8921, 1056) == 1

    sys.stdout.write("Part1 answer: {}\n".format(count_total_similarities_in_16_bits_part1(116, 299, 40000000)))
    sys.stdout.flush()

    sys.stdout.write("Part2 answer: {}\n".format(count_total_similarities_in_16_bits_part2(116, 299, 5000000)))
    sys.stdout.flush()

if __name__ == '__main__':
    main()
