def find_floor():
    input = ""

    with open("./2015/day_01_input.txt", "r") as f:
        input = f.read()

    floor_up = input.count("(")
    floor_down = input.count(")")

    return floor_up - floor_down


print(find_floor())
