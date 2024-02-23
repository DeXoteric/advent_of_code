import re


def day_06_p1():
    puzzle_input = ()
    lights = {}
    lights_on = 0

    with open("./2015/inputs/day_06_input.txt", "r") as f:
        puzzle_input = f.read().splitlines()

    for i in range(1000):
        for j in range(1000):
            lights[i, j] = 0

    for line in puzzle_input:
        if line.startswith("turn on"):
            lights = turn_on_lights(line, lights)
        elif line.startswith("turn off"):
            lights = turn_off_lights(line, lights)
        elif line.startswith("toggle"):
            lights = toggle_lights(line, lights)

    for light in lights:
        if lights[light] == 1:
            lights_on += 1

    return lights_on


def turn_on_lights(line, lights):
    coords = re.findall(r"\d+", line)
    start_x, start_y, end_x, end_y = tuple(map(int, coords))
    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            lights[i, j] = 1
    return lights


def turn_off_lights(line, lights):
    coords = re.findall(r"\d+", line)
    start_x, start_y, end_x, end_y = tuple(map(int, coords))
    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            lights[i, j] = 0
    return lights


def toggle_lights(line, lights):
    coords = re.findall(r"\d+", line)
    start_x, start_y, end_x, end_y = tuple(map(int, coords))
    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            lights[i, j] = 1 if lights[i, j] == 0 else 0
    return lights


print(day_06_p1())
