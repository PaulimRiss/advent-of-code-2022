def main():
    input = open("input.txt", "r").read()
    str_list = simplify_to_list(input)
    sum = first(str_list)
    print(sum)
    sum = second(str_list)
    print(sum)


def simplify_to_list(input):
    res = input.split("\n")[:-1]
    for i in range(len(res)):
        res[i] = res[i].split(",")
        for j in range(len(res[i])):
            res[i][j] = res[i][j].split("-")
            for k in range(len(res[i][j])):
                res[i][j][k] = int(res[i][j][k])
    return res


def first(arr_list):
    sum = 0
    for arr in arr_list:
        elf1 = set(range(arr[0][0], arr[0][1] + 1))
        elf2 = set(range(arr[1][0], arr[1][1] + 1))
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            sum += 1

    return sum


def second(arr_list):
    sum = 0
    for arr in arr_list:
        elf1 = set(range(arr[0][0], arr[0][1] + 1))
        elf2 = set(range(arr[1][0], arr[1][1] + 1))
        if len(elf1 & elf2):
            sum += 1

    return sum


if __name__ == "__main__":
    main()
