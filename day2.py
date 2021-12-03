f = open("day2.txt", "r").read().split("\n")
#f = "forward 5, down 5, forward 8, up 3, down 8, forward 2".split(", ")


def part1():
    horizontal = 0
    depth = 0

    for movement in f:
        direction, magnitude = movement.split(" ")
        magnitude = int(magnitude)
        if direction == "forward":
            horizontal += magnitude
        elif direction == "down":
            depth += magnitude
        elif direction == "up":
            depth -= magnitude

    return horizontal * depth


def part2():
    horizontal = 0
    depth = 0
    aim = 0

    for movement in f:
        direction, magnitude = movement.split(" ")
        magnitude = int(magnitude)
        if direction == "forward":
            horizontal += magnitude
            depth += aim * magnitude
        elif direction == "down":
            aim += magnitude
        elif direction == "up":
            aim -= magnitude

    return horizontal * depth


print(part1())
