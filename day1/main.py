def main():
    input = open("input.txt", "r").read()
    print(get_bigger_cal_elf(input))
    print(get_top_3_cal_elf(input))


# first part
def get_bigger_cal_elf(input):
    elfs = input.split("\n\n")
    for i in range(len(elfs)):
        elfs[i] = sum(
            [int(cal if cal.isnumeric() else 0) for cal in elfs[i].split("\n")]
        )

    return max(elfs)


# second part
def get_top_3_cal_elf(input):
    elfs = input.split("\n\n")
    for i in range(len(elfs)):
        elfs[i] = sum(
            [int(cal if cal.isnumeric() else 0) for cal in elfs[i].split("\n")]
        )

    top_three = sorted(elfs, reverse=True)[:3]

    return sum(top_three)


if __name__ == "__main__":
    main()
