import string


def day_05_p1():
    alphabet = tuple(string.ascii_lowercase)
    vowels = ("a", "e", "i", "o", "u")
    required_strings = tuple(map(lambda x: x + x, alphabet))
    forbidden_strings = ("ab", "cd", "pq", "xy")

    puzzle_input = ()

    with open("./2015/inputs/day_05_input.txt", "r") as f:
        puzzle_input = f.read().splitlines()

    nice_strings = 0

    for line in puzzle_input:
        if any(forb_string in line for forb_string in forbidden_strings):
            continue
        if sum(line.count(vowel) for vowel in vowels) < 3:
            continue
        if not any(req_string in line for req_string in required_strings):
            continue

        nice_strings += 1

    return nice_strings


print(day_05_p1())
