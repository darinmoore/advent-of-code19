OP_ARG_LEN = {1: 3, 2: 3, 3: 1, 4: 1,
              5: 2, 6: 2, 7: 3, 8: 3}

# Determines if args are imm or positions and returns final values, by 
# recognizing immediate or grabbing value from specified position
def get_args(instructions, args, arg_modes):
        final_args = []
        for i in range(len(args)):
            if arg_modes[i] == 1:
                final_args.append(args[i])
            else:
                final_args.append(instructions[args[i]])
        return final_args

def run_instructions(instructions):
    PC = 0
    while instructions[PC] % 100 != 99:
        op = instructions[PC] % 100
        pre_args = instructions[PC+1 : PC+OP_ARG_LEN[op]+1]
        # gets parameter modes in order
        arg_modes = list(str(instructions[PC])[:-2])[::-1]
        arg_modes = [int(x) for x in arg_modes]
        arg_modes = arg_modes + [0] * (len(pre_args) - len(arg_modes)) # pads missing zeros
        # Add
        if op == 1:
            arg_modes[-1] = 1
            args = get_args(instructions, pre_args, arg_modes)
            instructions[args[2]] = args[0] + args[1]
            PC += 4
        # Multiply
        elif op == 2:
            arg_modes[-1] = 1
            args = get_args(instructions, pre_args, arg_modes)
            instructions[args[2]] = args[0] * args[1]
            PC += 4
        # Store input
        elif op == 3:
            instructions[instructions[PC+1]] = int(input("Input an integer: "))
            PC += 2
        # Read output
        elif op == 4:
            print("OUTPUT: ", instructions[instructions[PC+1]])
            PC += 2
        # Jump if true
        elif op == 5:
            args = get_args(instructions, pre_args, arg_modes)
            if args[0] != 0:
                PC = args[1]
            else:
                PC += 3
        # Jump if false
        elif op == 6:
            args = get_args(instructions, pre_args, arg_modes)
            if args[0] == 0:
                PC = args[1]
            else:
                PC += 3
        # Bool Less Than
        elif op == 7:
            arg_modes[-1] = 1
            args = get_args(instructions, pre_args, arg_modes)
            if args[0] < args[1]:
                instructions[args[2]] = 1
            else:
                instructions[args[2]] = 0
            PC += 4
        # Bool Equals
        elif op == 8:
            arg_modes[-1] = 1
            args = get_args(instructions, pre_args, arg_modes)
            if args[0] == args[1]:
                instructions[args[2]] = 1
            else:
                instructions[args[2]] = 0
            PC += 4

def part1(instructions):
    # Input 1 when prompted
    run_instructions(instructions)

def part2(instructions):
    # Input 5 when prompted
    pass

if __name__ == "__main__":
    #instructions = [int(x) for x in  open('test.txt').read().split(',')]
    instructions = [int(x) for x in  open('input1.txt').read().split(',')]
    saved_copy = instructions.copy()

    print("Part 1: ")
    part1(instructions)
