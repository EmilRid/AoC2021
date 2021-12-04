f = open("day3/day3.txt", "r").read().split("\n")
#f = "00100 11110 10110 10111 10101 01111 00111 11100 10000 11001 00010 01010".split(" ")


def part1():
    gamma = ""
    epsilon = ""
    for i in range(len(f[0])):
        zeros = 0
        ones = 0
        for byte in f:
            if byte[i] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


def part2():
    list1 = f
    for column in range(len(f[0])):
        list2 = []
        zeros = 0
        ones = 0
        for byte in list1:
            first = byte[column]
            if first == "1":
                ones += 1
            elif first == "0":
                zeros += 1

        if ones >= zeros:
            for byte in list1:
                if byte[column] == "1":
                    list2.append(byte)

        elif zeros > ones:
            for byte in list1:
                if byte[column] == "0":
                    list2.append(byte)

        list1 = list2
        list2.clear

        if len(list1) == 1:
            oxygen = list1[0]
            break

    list1 = f
    for column in range(len(f[0])):
        list2 = []
        zeros = 0
        ones = 0
        for byte in list1:
            first = byte[column]
            if first == "1":
                ones += 1
            elif first == "0":
                zeros += 1

        if ones < zeros:
            for byte in list1:
                if byte[column] == "1":
                    list2.append(byte)

        elif zeros <= ones:
            for byte in list1:
                if byte[column] == "0":
                    list2.append(byte)

        list1 = list2
        list2.clear

        if len(list1) == 1:
            co2 = list1[0]
            break

    return int(oxygen, 2) * int(co2, 2)


print(part2())
