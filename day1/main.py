def main():
    input = open("input.txt", "r").read()
    elfs = simplify_to_list(input)
    print(get_bigger_cal_elf(elfs))
    print(get_top_3_cal_elf(elfs))


def simplify_to_list(input):
    res = input.split("\n\n")
    for i in range(len(res)):
        res[i] = sum([int(cal if cal.isnumeric() else 0) for cal in res[i].split("\n")])
    return res


# first part
def get_bigger_cal_elf(elfs):
    return max(elfs)


# second part
def get_top_3_cal_elf(elfs):
    top_three = sorted(elfs, reverse=True)[:3]

    return sum(top_three)


if __name__ == "__main__":
    main()
