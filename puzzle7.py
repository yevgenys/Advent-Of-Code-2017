import re
from collections import namedtuple

SPLITTER = re.compile("(?P<name>\w+)\s\((?P<weight>\d+)\)\s?-?>?\s?(?P<links>[a-z, ]+)?")


def read_input():
    with open("./puzzle7_input", 'r') as f:
        return f.read().splitlines()


def split_link_names(line):
    return map(lambda l: l.strip(), line.split(","))


def find_top_node_name(input_):
    children = []
    nodes = []
    for line in input_:
        m = SPLITTER.match(line)
        assert m
        name = m.group("name")
        nodes.append(name)
        if m.group("links"):
            map(children.append, split_link_names(m.group("links")))
    return filter(lambda n: n not in children, nodes)[0]


Node = namedtuple("Node", ["name", "weight", "children"])


def build_tree(name, raw_input_):
    for node in raw_input_:
        m = SPLITTER.match(node)
        assert m
        if name == m.group("name"):
            if m.group("links"):
                children = map(lambda n: build_tree(n, raw_input_), split_link_names(m.group("links")))
            else:
                children = None
            return Node(name, int(m.group("weight")), children)


def count_branch(node):
    return sum(map(lambda c: c.weight, node.children)) + node.weight


def get_unbalanced_weights(node):
    if node.children is None:
        return node.weight

    expected_line_weight = -1
    sm = node.weight
    for child in node.children:
        weight = get_unbalanced_weights(child)
        sm += weight
        if expected_line_weight == -1:
            expected_line_weight = weight
        elif expected_line_weight != weight:
            print("Expected '{}' weight {} != {}; diff = {}".format(child.name, weight, expected_line_weight, expected_line_weight-weight))
    return sm


if __name__ == '__main__':
    test_in = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""
    assert find_top_node_name(test_in.splitlines()) == "tknk"

    print(get_unbalanced_weights(build_tree("tknk", test_in.splitlines())))

    actual_input = read_input()
    top_node_name = find_top_node_name(actual_input)
    print(top_node_name)
    get_unbalanced_weights(build_tree(top_node_name, actual_input))
