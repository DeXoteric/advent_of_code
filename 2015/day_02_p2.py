def calculate_total_ribbon_length():
    puzzle_input = ()

    with open("./2015/inputs/day_02_input.txt", "r") as f:
        puzzle_input = f.read().splitlines()

    puzzle_input = list(map(lambda x: x.split("x"), puzzle_input))

    total_ribbon_length = 0

    for line in puzzle_input:
        line = sorted(map(lambda x: int(x), line))

        ribbon_length = 2 * line[0] + 2 * line[1]
        bow_ribbon_length = line[0] * line[1] * line[2]

        total_ribbon_length += ribbon_length + bow_ribbon_length

    return total_ribbon_length


print(calculate_total_ribbon_length())
