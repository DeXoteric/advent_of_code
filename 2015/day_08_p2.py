def day_08_p2():
    puzzle_input = ()
    result = 0

    with open("./2015/inputs/day_08_input.txt", "r") as f:
        puzzle_input = f.read().splitlines()

    for line in puzzle_input:
        number_of_all_characters = len(line)
        number_of_characters_in_new_string = (
            len(line) + 2 + line.count("\\") + line.count('"')
        )
        result += number_of_characters_in_new_string - number_of_all_characters

    return result


print(day_08_p2())
