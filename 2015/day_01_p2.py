def find_first_negative_number():
    input = ""

    with open("./2015/day_01_input.txt", "r") as f:
        input = f.read()

    input = list(input)

    floor_number = 0
    iteration = 0

    for character in input:
        if character == "(":
            floor_number += 1
        else:
            floor_number -= 1
        iteration += 1
        if floor_number < 0:
            return iteration


print(find_first_negative_number())
