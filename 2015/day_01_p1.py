def day_01_p1():
    puzzle_input = ""

    with open("./2015/inputs/day_01_input.txt", "r") as f:
        puzzle_input = f.read()

    floor_up = puzzle_input.count("(")
    floor_down = puzzle_input.count(")")

    return floor_up - floor_down


print(day_01_p1())
