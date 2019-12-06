def build_map(orbits):
    planets = set()
    solar_system = {}
    for orbit in orbits:
        solar_system[orbit[1]] = orbit[0]
        planets.add(orbit[0])
        planets.add(orbit[1])
    return planets, solar_system

def get_orbits(num_orbits_dict, planet, solar_system):
    if planet not in num_orbits_dict:
        if planet in solar_system:
            num_orbits_dict[planet] = 1 + get_orbits(num_orbits_dict, 
                                                     solar_system[planet], 
                                                     solar_system)
        else:
            num_orbits_dict[planet] = 0
    return num_orbits_dict[planet]

def part1(planets, solar_system):
    return sum([get_orbits({}, planet, solar_system) for planet in planets])

def part2(solar_system):
    my_planet = solar_system["YOU"]
    santa_planet = solar_system["SAN"]
    path = []
    while my_planet != "COM":
        path.append(my_planet)
        my_planet = solar_system[my_planet]
    santa_transfers = 0
    while santa_planet not in path:
        santa_transfers += 1
        santa_planet = solar_system[santa_planet]
    return santa_transfers + path.index(santa_planet)


if __name__ == "__main__":
    with open("input1.txt") as f:
        lines = f.readlines()
    orbits = [line.strip().split(")") for line in lines]
    planets, solar_system = build_map(orbits)

    print("Part1: " + str(part1(planets, solar_system)))
    print("Part2: " + str(part2(solar_system)))