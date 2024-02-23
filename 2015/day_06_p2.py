import re


def day_06_p2():
    puzzle_input = ()
    lights = {}
    total_brightness = 0

    with open("./2015/inputs/day_06_input.txt", "r") as f:
        puzzle_input = f.read().splitlines()

    for i in range(1000):
        for j in range(1000):
            lights[i, j] = 0

    for line in puzzle_input:
        if line.startswith("turn on"):
            lights = brightness_up(line, lights)
        elif line.startswith("turn off"):
            lights = brightness_down(line, lights)
        elif line.startswith("toggle"):
            lights = brightness_twice_up(line, lights)

    for light in lights:
        total_brightness += lights[light]

    return total_brightness


def brightness_up(line, lights):
    coords = re.findall(r"\d+", line)
    start_x, start_y, end_x, end_y = tuple(map(int, coords))
    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            lights[i, j] += 1
    return lights


def brightness_down(line, lights):
    coords = re.findall(r"\d+", line)
    start_x, start_y, end_x, end_y = tuple(map(int, coords))
    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            lights[i, j] -= 1 if lights[i, j] > 0 else 0
    return lights


def brightness_twice_up(line, lights):
    coords = re.findall(r"\d+", line)
    start_x, start_y, end_x, end_y = tuple(map(int, coords))
    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            lights[i, j] += 2
    return lights


print(day_06_p2())
