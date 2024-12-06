# https://adventofcode.com/2024/day/2
# https://adventofcode.com/2024/day/2#part2
#
# one report per line.
# Each report is a list of numbers called levels that are separated by spaces.
# For example:
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
#
# This example data contains six reports each containing five levels.
#
# determine if report is "safe":
#   - The levels are either all increasing or all decreasing.
#   - Any two adjacent levels differ by at least one and at most three.

def soft_increasing(a):
    # checks if 'a' is soft increasing strictly
    pval = a[0]
    for val in a[1:]:
        if pval >= val or val - pval > 3:
            return False
        pval = val
    return True

def soft_increasing_dampened(a, dampen_protection = True):
    # checks if 'a' is soft increasing strictly, ignore if it fails once
    pval = a[0]
    for val in a[1:]:
        if pval >= val or val - pval > 3:
            if dampen_protection:
                dampen_protection = False
                continue
            return False
        pval = val
    return True

def soft_decreasing(a):
    # checks if 'a' is soft decreasing strictly
    pval = a[0]
    for val in a[1:]:
        if pval <= val or pval - val > 3:
            return False
        pval = val
    return True

def soft_decreasing_dampened(a, dampen_protection = True):
    # checks if 'a' is soft decreasing strictly, ignore if fails once
    pval = a[0]
    for val in a[1:]:
        if pval <= val or pval - val > 3:
            if dampen_protection:
                dampen_protection = False
                continue
            return False
        pval = val
    return True

def solution_1(f):
    safe = 0
    for line in f:
        report = [int(v) for v in line.split()]
        if soft_increasing(report) or soft_decreasing(report):
            safe += 1

    return safe

def solution_2(f):
    safe = 0
    failed = []
    for line in f:
        report = [int(v) for v in line.split()]
        if soft_increasing_dampened(report) or soft_decreasing_dampened(report):
            safe += 1
        elif soft_increasing_dampened(report[1:], False) or soft_decreasing_dampened(report[1:], False):
            safe += 1
        else:
            failed.append(report)
    return safe, failed

def main():
    with open('d2_input.txt', 'r') as f:
        print(solution_1(f))
        # restart looking at file (probably needed)
        f.seek(0)
        safe, failed = solution_2(f)
        print(safe)
        print(failed)


if __name__ == '__main__':
    main()