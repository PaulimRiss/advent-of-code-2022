ME = {"X": 1, "Y": 2, "Z": 3}
OPPONENT = {"A": ME["X"], "B": ME["Y"], "C": ME["Z"]}
OUTCOME = {"WIN": 6, "DRAW": 3, "LOSS": 0}


def main():
    input = open("input.txt", "r").read()
    str_list = simplify_to_list(input)
    total_score = count_total_score1(str_list)
    print(total_score)
    total_score = count_total_score_2(str_list)
    print(total_score)


def simplify_to_list(input):
    res = input.split("\n")[:-1]
    return res


def count_total_score1(str_list):
    total_score = 0
    for str in str_list:
        total_score += (
            ME[str[-1]]
            + OUTCOME["WIN"] * (ME[str[-1]] == round((OPPONENT[str[0]] + 1) % 3.1))
            + OUTCOME["DRAW"] * (ME[str[-1]] == OPPONENT[str[0]])
            + OUTCOME["LOSS"] * (round((ME[str[-1]] + 1) % 3.1) == OPPONENT[str[0]])
        )
    return total_score


def count_total_score_2(str_list):
    total_score = 0
    for str in str_list:
        total_score += (
            (OUTCOME["WIN"] + round((OPPONENT[str[0]] + 1) % 3.1)) * (str[-1] == "Z")
            + (OUTCOME["DRAW"] + OPPONENT[str[0]]) * (str[-1] == "Y")
            + (OUTCOME["LOSS"] + (OPPONENT[str[0]] - 1 if str[0] != "A" else 3))
            * (str[-1] == "X")
        )
    return total_score


if __name__ == "__main__":
    main()
