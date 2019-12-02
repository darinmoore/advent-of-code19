def calc_fuel(x):
    return x // 3 - 2

def calc_fuel_recur(x):
    total = 0
    while x > 8: # 8 is max number for calc_fuel to be 0
        x = calc_fuel(x)
        total += x
    return total

def part1(mods):
    return sum([calc_fuel(mod) for mod in mods])

def part2(mods):
    return sum([calc_fuel_recur(mod) for mod in mods])

if __name__ == '__main__':
    with open('input1.txt') as f:
        lines = f.readlines()

    mods = [int(line) for line in lines]
    print("Part 1: " + str(part1(mods)))
    print("Part 2: " + str(part2(mods)))