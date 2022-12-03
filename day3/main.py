import string


def main():
    input = open("input.txt", "r").read()
    str_list = simplify_to_list(input)
    sum = sum_dup_priorities(str_list)
    print(sum)
    sum = sum_badges_priorities(str_list)
    print(sum)


def simplify_to_list(input):
    res = input.split("\n")[:-1]
    return res


PRIORITY = [None, *list(string.ascii_lowercase + string.ascii_uppercase)]


def sum_dup_priorities(str_list):
    sum = 0
    for str in str_list:
        first_comp = set(str[: len(str) // 2])
        second_comp = set(str[len(str) // 2 :])
        sum += PRIORITY.index((first_comp & second_comp).pop())
    return sum


def sum_badges_priorities(str_list):
    sum = 0
    new_list = []
    for i in range(0, len(str_list), 3):
        new_list.append(str_list[i : i + 3])
    for group in new_list:
        sum += PRIORITY.index((set(group[0]) & set(group[1]) & set(group[2])).pop())

    return sum


if __name__ == "__main__":
    main()
