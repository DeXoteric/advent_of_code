import re


def day_08_p1():
    puzzle_input = ()
    result = 0

    with open("./2015/inputs/day_08_input.txt", "r") as f:
        puzzle_input = f.read().splitlines()

    for line in puzzle_input:
        number_of_all_characters = len(line)
        number_of_characters_in_memory = (
            len(line[1:-1])
            - line.count("\\\\")
            - line[1:-1].count('\\"')
            - (len(re.findall(r"\\x[0-9a-fA-F]{2}", line)) * 3)
        )
        result += number_of_all_characters - number_of_characters_in_memory

    return result


print(day_08_p1())
