# https://adventofcode.com/2024/day/3
# https://adventofcode.com/2024/day/3#part2
#
# Very simply part 1:
#   1. use regex to find all valid multiplications
#   2. use regex groups to find the numbers to multiply
#   3. gather total
#

import re

# Essentially, look for mul(X,Y) ops and make separate groups for the numbers
regex_1 = "mul\(([0-9]{1,3}),([0-9]{1,3})\)"

# Edit from regex 1, need to track operation now so operation name is now a group.
# Then add do and don't to the mix and job done
regex_2 = "(mul)\(([0-9]{1,3}),([0-9]{1,3})\)|(do)\(\)|(don't)\(\)"

def solution_1(f):
    total = 0
    for line in f:
        muls = re.findall(regex_1, line)
        for op in muls:
            total += int(op[0]) * int(op[1])
    return total

def solution_2(f):
    total = 0
    enabled = True
    for line in f:
        ops = re.findall(regex_2, line)
        for op in ops:
            print(op)
            if op[3] == 'do':
                enabled = True
            elif op[4] == "don't":
                enabled = False
            elif op[0] == 'mul' and enabled:
                total += int(op[1]) * int(op[2])
    return total

def main():
    with open('d3_input.txt', 'r') as f:
        print(solution_1(f))
        f.seek(0)
        print(solution_2(f))


if __name__ == '__main__':
    main()