PLAYS = {
    "A": ("A", "B", "C", 1),
    "B": ("B", "C", "A", 2),
    "C": ("C", "A", "B", 3),
}


def main():
    input = open("input.txt", "r").read()
    str_list = simplify_to_list(input)
    total_score = count_total_score1(str_list)
    print(total_score)
    total_score = count_total_score_2(str_list)
    print(total_score)


class HandPlay:
    def __init__(self, char):
        self.played = PLAYS[char][0]
        self.counterplay = PLAYS[char][1]
        self.winplay = PLAYS[char][2]
        self.score = PLAYS[char][3]

    def battle(self, other):
        if self.played == other.counterplay:
            return 6
        elif self.played == other.played:
            return 3
        else:
            return 0


def simplify_to_list(input):
    res = input.split("\n")[:-1]
    return res


def count_total_score1(str_list):
    total_score = 0
    MY_PLAYS = {"X": "A", "Y": "B", "Z": "C"}
    for str in str_list:
        opponent_play = HandPlay(str[0])
        my_play = HandPlay(MY_PLAYS[str[-1]])
        total_score += my_play.score + my_play.battle(opponent_play)

    return total_score


def count_total_score_2(str_list):
    total_score = 0
    for str in str_list:
        opponent_play = HandPlay(str[0])
        match str[-1]:
            case "X":
                my_play = HandPlay(opponent_play.winplay)
            case "Y":
                my_play = HandPlay(opponent_play.played)
            case "Z":
                my_play = HandPlay(opponent_play.counterplay)
        total_score += my_play.score + my_play.battle(opponent_play)
    return total_score


if __name__ == "__main__":
    main()
