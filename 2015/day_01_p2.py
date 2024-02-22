def find_first_negative_number():
    puzzle_input = ""

    with open("./2015/inputs/day_01_input.txt", "r") as f:
        puzzle_input = f.read()

    puzzle_input = list(puzzle_input)

    floor_number = 0
    iteration = 0

    for character in puzzle_input:
        if character == "(":
            floor_number += 1
        else:
            floor_number -= 1
        iteration += 1
        if floor_number < 0:
            return iteration


print(find_first_negative_number())
