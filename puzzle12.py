def read_input():
    with open("puzzle12_input", "r") as f:
        return f.read().splitlines()


def create_links(lst):
    db = {}
    for line in lst:
        digit, links = line.split("<->")
        digit = digit.strip()
        db_links = db.get(digit, set())
        map(db_links.add, map(lambda d: d.strip(), links.split(",")))
        db[digit] = db_links
    return db


def has_connection(hastable, digit, visited):
    links = hastable.get(digit, set())
    if digit == "0" or "0" in links:
        return True

    for link in links:
        if link in visited:
            continue
        visited.append(link)
        if has_connection(hastable, link, visited):
            return True

    return None


def count_zero_group_nodes(hastable):
    counter = 0
    for digit in hastable:
        if has_connection(hastable, digit, []):
            counter += 1
    return counter


def count_groups(hastable):
    counter = 0
    visited = []
    for digit in hastable:
        if digit in visited:
            continue
        counter += 1

        node = [digit]
        while node:
            n = node.pop()
            for sub_node in hastable.get(n, set()):
                if sub_node not in visited:
                    visited.append(sub_node)
                    node.append(sub_node)

    return counter


if __name__ == '__main__':
    test_in = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

    assert count_zero_group_nodes(create_links(test_in.splitlines())) == 6
    print(count_groups(create_links(test_in.splitlines())))
    assert count_groups(create_links(test_in.splitlines())) == 2

    table = create_links(read_input())
    print(count_zero_group_nodes(table))
    print(count_groups(table))
