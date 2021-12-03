
f = [int(n) for n in open("day1.txt", "r").read().split("\n")]
#f = [int(n) for n in "199 200 208 210 200 207 240 269 260 263".split(" ")]


def part1():

    total = 0
    lastmeasure = f[0]
    for measurement in f:
        if measurement > lastmeasure:
            total += 1
        lastmeasure = measurement
    return total + 1


def part2():
    print(f)
    total = 0
    lastmeasure = f[0] + f[1] + f[2]
    for index in range(len(f) - 1):
        if index <= len(f) - 3:
            measure = f[index] + f[index + 1] + f[index + 2]
            if measure > lastmeasure:
                total += 1
        lastmeasure = measure

    return total
