def read_input():
    with open("./puzzle4_input", 'r') as f:
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
            sorted_phrase = sorted(phrase)
            if sorted_phrase in visited:
                break
            visited.append(sorted_phrase)
        else:
            valid += 1
    return valid


if __name__ == '__main__':
    in_ = read_input()
    print(count_valid_phrases(in_))
    print(count_valid_phrases_no_anagrams(in_))
