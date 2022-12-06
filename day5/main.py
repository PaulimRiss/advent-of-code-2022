def main():
    input = open("input.txt", "r").read()
    stack1 = StackCrates(input)
    print(stack1.phase_1())
    stack2 = StackCrates(input)
    print(stack2.phase_2())


class StackCrates:
    def __init__(self, ext_input):
        self.stacksstr = ext_input.split("\n ")[0]
        self.stacks = self.__turn_input_into_dict(self.stacksstr)
        self.commandsstr = ext_input.split("\n\n")[1]
        self.commands = self.__turn_commands_into_list(self.commandsstr)

    def __turn_commands_into_list(self, input):
        input = input.strip().split("\n")
        for i in range(len(input)):
            input[i] = list(
                map(
                    lambda x: int(x),
                    list(filter(lambda x: x.isdigit(), input[i].split(" "))),
                )
            )

        return input

    def __turn_input_into_dict(self, input):
        input_list = [dict(enumerate(i)) for i in input.split("\n")]
        for i in range(len(input_list)):
            input_list[i] = {
                (k - 1) // 4 + 1: v for k, v in input_list[i].items() if v not in " []"
            }
        stacks = {}
        for i in input_list:
            for k, v in i.items():
                if k not in stacks:
                    stacks[k] = [v]
                else:
                    stacks[k].append(v)
        return {k: v[::-1] for k, v in stacks.items()}

    def __unstack_n_times(self, stack, n):
        unstacked = []
        while n > 0 and len(self.stacks[stack]) > 0:
            unstacked.append(self.stacks[stack].pop())
            n -= 1
        return unstacked

    def __unstack_n_crates(self, stack, n):
        return self.__unstack_n_times(stack, n)[::-1]

    def __stack_list(self, stack, list):
        self.stacks[stack].extend(list)

    def __change_n_to_stack_CrateMover_9000(self, n, stack1, stack2):
        unstacked = self.__unstack_n_times(stack1, n)
        self.__stack_list(stack2, unstacked)

    def __change_n_to_stack_CrateMover_9001(self, n, stack1, stack2):
        unstacked = self.__unstack_n_crates(stack1, n)
        self.__stack_list(stack2, unstacked)

    def __return_top_stacks(self):
        top_stacks = []
        for i in range(1, len(self.stacks) + 1):
            top_stacks.append(self.stacks[i][-1])
        return "".join(top_stacks)

    def phase_1(self):
        for i in self.commands:
            self.__change_n_to_stack_CrateMover_9000(i[0], i[1], i[2])
        return self.__return_top_stacks()

    def phase_2(self):
        for i in self.commands:
            self.__change_n_to_stack_CrateMover_9001(i[0], i[1], i[2])
        return self.__return_top_stacks()


if __name__ == "__main__":
    main()
