from puzzle10 import knot_hash, sparse_hash, create_single_hash_from_sparse_hashs


M_N = 128


def to_bin(hex):
    return "".join(bin(int(d, 16))[2:].zfill(4) for d in hex)


def _hash(key):
    arr = map(ord, key)
    answ = knot_hash(arr, 64)
    return create_single_hash_from_sparse_hashs(map(hex, sparse_hash(answ)))


def part_1(grid):
    return sum(len(filter(lambda d: d == "#", line)) for line in grid)


def draw_grid(key):
    grid = []
    for i in xrange(M_N):
        grid.append([i for i in to_bin(_hash(key.format(i))).replace("1", "#")])
    return grid


def tag_region(grid, start_points, tag):
    x, y = start_points
    if x > M_N or y > M_N:
        return

    grid[x][y] = tag
    right_y = y + 1
    if right_y < M_N and grid[x][right_y] == "#":
        grid[x][right_y] = tag
        tag_region(grid, (x, right_y), tag)

    down_x = x + 1
    if down_x < M_N and grid[down_x][y] == "#":
        grid[down_x][y] = tag
        tag_region(grid, (down_x, y), tag)

    left_y = y - 1
    if left_y >= 0 and grid[x][left_y] == "#":
        grid[x][left_y] = tag
        tag_region(grid, (x, left_y), tag)

    up_x = x - 1
    if up_x >= 0 and grid[up_x][y] == "#":
        grid[up_x][y] = tag
        tag_region(grid, (up_x, y), tag)


def calc_regions(grid):
    cur_region = "1"
    for i, line in enumerate(grid):
        for j, digit in enumerate(line):
            if digit == "#":
                tag_region(grid, (i, j), cur_region)
                cur_region = str(int(cur_region) + 1)
    return int(cur_region) - 1


def print_grid(grid):
    for line in grid:
        for el in line:
            print el.ljust(4),
        print


if __name__ == '__main__':
    grid = draw_grid("wenycdww-{}")
    print(part_1(grid))

    print(calc_regions(grid))
    print_grid(grid)
