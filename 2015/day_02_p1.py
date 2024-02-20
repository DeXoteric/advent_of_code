def calculate_total_square_feet_of_wrapping_paper():
    input = ()

    with open("./2015/day_02_input.txt", "r") as f:
        input = f.read().splitlines()

    input = list(map(lambda x: x.split("x"), input))

    total_box_surface_area = 0
    total_extra_surface_area = 0

    for line in input:
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


print(calculate_total_square_feet_of_wrapping_paper())
