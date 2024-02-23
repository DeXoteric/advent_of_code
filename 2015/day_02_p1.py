def day_02_p1():
    puzzle_input = ()

    with open("./2015/inputs/day_02_input.txt", "r") as f:
        puzzle_input = f.read().splitlines()

    puzzle_input = list(map(lambda x: x.split("x"), puzzle_input))

    total_box_surface_area = 0
    total_extra_surface_area = 0

    for line in puzzle_input:
        length, width, height = map(lambda x: int(x), line)

        box_surface_area = 2 * length * width + 2 * width * height + 2 * length * height
        total_box_surface_area += box_surface_area

        extra_surface_area = sorted(
            (
                length * width,
                width * height,
                length * height,
            )
        )
        total_extra_surface_area += extra_surface_area[0]

    return total_box_surface_area + total_extra_surface_area


print(day_02_p1())
