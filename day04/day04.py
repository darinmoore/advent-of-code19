def has_repeated_digit(number):
    digits = str(number)
    for digit in set(digits):
        if digits.count(digit) >= 2:
            return True
    return False

def has_digits_increasing(number):
    digits = str(number)
    for i in range(1, len(digits)):
        if digits[i] < digits[i-1]:
            return False
    return True

# Two matching digits not part of larger group of matching digits
def has_repeat_double_digit(number):
    digits = str(number)
    for digit in set(digits):
        if digits.count(digit) == 2:
            return True
    return False

def part1(min_num, max_num):
    possible_nums = range(min_num, max_num)
    possible_nums = [num for num in possible_nums if has_digits_increasing(num)]
    possible_nums = [num for num in possible_nums if has_repeated_digit(num)]
    return len(possible_nums)

def part2(min_num, max_num):
    possible_nums = range(min_num, max_num)
    possible_nums = [num for num in possible_nums if has_digits_increasing(num)]
    possible_nums = [num for num in possible_nums if has_repeat_double_digit(num)]
    return len(possible_nums)

if __name__ == "__main__":
    min_num = 136760
    max_num = 595730

    print("Part1: " + str(part1(min_num, max_num)))
    print("Part2: " + str(part2(min_num, max_num)))