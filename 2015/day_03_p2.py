def day_03_p2():
    puzzle_input = ()

    with open("./2015/inputs/day_03_input.txt", "r") as f:
        puzzle_input = tuple(f.read())

    visited_houses = [(0, 0)]
    last_visited_house = [0, 0]

    for direction in puzzle_input[1::2]:
        if direction == "^":
            last_visited_house = (last_visited_house[0] + 1, last_visited_house[1])
        elif direction == ">":
            last_visited_house = (last_visited_house[0], last_visited_house[1] + 1)
        elif direction == "v":
            last_visited_house = (last_visited_house[0] - 1, last_visited_house[1])
        elif direction == "<":
            last_visited_house = (last_visited_house[0], last_visited_house[1] - 1)
        visited_houses.append(last_visited_house)

    last_visited_house = [0, 0]

    for direction in puzzle_input[::2]:
        if direction == "^":
            last_visited_house = (last_visited_house[0] + 1, last_visited_house[1])
        elif direction == ">":
            last_visited_house = (last_visited_house[0], last_visited_house[1] + 1)
        elif direction == "v":
            last_visited_house = (last_visited_house[0] - 1, last_visited_house[1])
        elif direction == "<":
            last_visited_house = (last_visited_house[0], last_visited_house[1] - 1)
        visited_houses.append(last_visited_house)

    return len(set(visited_houses))


print(day_03_p2())
