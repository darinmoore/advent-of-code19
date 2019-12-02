def do_op(instructions, op, pos1, pos2, store):
    if op == 1:
        instructions[store] = instructions[pos1] + instructions[pos2]
    if op == 2:
        instructions[store] = instructions[pos1] * instructions[pos2]

def run_instructions(instructions):
    PC = 0
    while instructions[PC] != 99:
        do_op(instructions, instructions[PC], instructions[PC+1],
              instructions[PC+2], instructions[PC+3])
        PC += 4
    return instructions[0]

def part1(instructions):
    instructions[1] = 12
    instructions[2] = 2
    return run_instructions(instructions)

def part2(instructions):
    for i in range(100):
        for j in range(100):
            prog = instructions.copy()
            prog[1] = i
            prog[2] = j
            if run_instructions(prog) == 19690720:
                return 100 * i + j


if __name__ == "__main__":
    with open('input1.txt') as f:
        line = f.readlines()

    instructions = [int(char) for char in line[0].split(',')]
    saved_copy = instructions.copy()

    print('Part1: ' + str(part1(instructions)))
    print('Part2: ' + str(part2(saved_copy)))