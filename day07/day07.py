import itertools

OP_ARG_LEN = {1: 3, 2: 3, 3: 1, 4: 1,
              5: 2, 6: 2, 7: 3, 8: 3, 99 : 0}

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

def run_instructions(instructions, phase, prev_output, PC):
    output = 0
    phase_used = False
    while True:
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
            if not phase_used:
                instructions[instructions[PC+1]] = phase
                phase_used = True
            else:
                instructions[instructions[PC+1]] = prev_output
            PC += 2
        # Read output
        elif op == 4:
            output = instructions[instructions[PC+1]]
            #print("OUTPUT: ", output)
            PC += 2
            break
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
        elif op == 99:
            return None, PC
    return output, PC

def part1(instructions):
    # run_instructions(instructions)
    phases_perm = list(itertools.permutations(range(5)))
    max_output = float("-inf") # Min int in python
    for phases in phases_perm:
        prev_output = 0
        for phase in phases:
            new_instructions = instructions.copy()
            prev_output, _ = run_instructions(new_instructions, phase, prev_output, 0)
        max_output = max(max_output, prev_output)
    return max_output

def part2(instructions):
    phases_perm = list(itertools.permutations(range(5,10)))
    max_output = float("-inf")
    for phases in phases_perm:
        # Creates instructions for each amplifier, parallel to phases
        machine_instructions = [instructions.copy() for i in range(5)] 
        PC_tracker           = [0 for i in range(5)]
        running              = [True] * 5
        amp = 0
        prev_output = 0
        final_output = 0
        while True:
            if running[amp]:
                prev_output, PC = run_instructions(machine_instructions[amp], 
                                                   phases[amp], prev_output, 
                                                   PC_tracker[amp])
                PC_tracker[amp] = PC
                if prev_output == None: 
                    break
                if amp == 4:
                    final_output = prev_output
            amp = (amp + 1) % 5
        max_output = max(max_output, final_output)
    return max_output

if __name__ == "__main__":
    #instructions = [int(x) for x in  open('test.txt').read().split(',')]
    instructions = [int(x) for x in  open('input1.txt').read().split(',')]

    print("Part 1: ", str(part1(instructions.copy())))
    print("Part 2: ", str(part2(instructions.copy())))
