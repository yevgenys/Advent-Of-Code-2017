def read_input():
    with open("./puzzle_input", 'r') as f:
        return f.read()


def count_valid_phrases(input_):
    valid = 0
    for line in input_.splitlines():
        visited = []
        for phrase in line.split(" "):
            if phrase in visited:
                break
            visited.append(phrase)
        else:
            valid += 1
    return valid


def count_valid_phrases_no_anagrams(input_):
    valid = 0
    for line in input_.splitlines():
        visited = []
        for phrase in line.split(" "):
            if phrase in visited:
                break
            visited.append(phrase)
        else:
            if not list_contains_anagram(visited):
                valid += 1
    return valid


def list_contains_anagram(lst):
    for i in xrange(len(lst)):
        check_element = sorted(lst[i])
        for j, el in enumerate(lst):
            if i == j:
                continue
            if sorted(el) == check_element:
                return True


if __name__ == '__main__':
    in_ = read_input()
    print(count_valid_phrases(in_))
    print(count_valid_phrases_no_anagrams(in_))
