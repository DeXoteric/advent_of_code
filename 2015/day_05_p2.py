import string
from itertools import product


def find_nice_strings():
    alphabet = tuple(string.ascii_lowercase)
    puzzle_input = ()
    nice_strings = 0

    with open("./2015/day_05_input.txt", "r") as f:
        puzzle_input = f.read().splitlines()

    # fancy for loop
    pairs = ["".join(pair) for pair in product(alphabet, repeat=2)]

    for line in puzzle_input:
        has_pair_of_two_letters = any(line.count(pair) >= 2 for pair in pairs)
        has_pair_outside_letter = any(
            line[i] == line[i + 2] for i in range(len(line) - 2)
        )
        if has_pair_of_two_letters and has_pair_outside_letter:
            nice_strings += 1

    return nice_strings


print(find_nice_strings())
