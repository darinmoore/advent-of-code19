def man_dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

def total_steps(pt, steps1, steps2):
    return steps1[pt] + steps2[pt]

def tuple_add(tup1, tup2):
    return tuple(map(sum, zip(tup1, tup2)))

def populate_map(wire1, wire2):
    delta = {'L' : (0,-1) , 'R': (0,1), 'U' : (1,0), 'D': (-1,0)}

    path1 = set()
    curr_pos = (0,0)
    steps1 = {}
    step = 0
    for move in wire1:
        for i in range(int(move[1:])):
            curr_pos = tuple_add(curr_pos, delta[move[0]])
            path1.add(curr_pos)
            step += 1
            steps1[curr_pos] = step

    path2 = set()
    curr_pos = (0,0)
    steps2 = {}
    step = 0
    for move in wire2:
        for i in range(int(move[1:])):
            curr_pos = tuple_add(curr_pos, delta[move[0]])
            path2.add(curr_pos)
            step += 1
            steps2[curr_pos] = step

    return path1, path2, steps1, steps2

def part1(path1, path2):
    man_dists = [man_dist((0,0), pt) for pt in (path1 & path2)]
    return min(man_dists)

def part2(path1, path2, steps1, steps2):
    step_dists = [total_steps(pt, steps1, steps2) for pt in (path1 & path2)]
    return min(step_dists)

if __name__ == "__main__":
    with open('input1.txt') as f:
        lines = f.readlines()

    lines = [l.strip().split(',') for l in lines]

    wire1 = lines[0]
    wire2 = lines[1]

    path1, path2, steps1, steps2 = populate_map(wire1, wire2)

    print("Part1: " + str(part1(path1, path2)))
    print("Part2: " + str(part2(path1, path2, steps1, steps2)))