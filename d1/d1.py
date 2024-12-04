# https://adventofcode.com/2024/day/1
# https://adventofcode.com/2024/day/1#part2
# basically sum the differences between a sorted list
# input is unsorted so just sort it, then loop and sum the difference

def solution_1():
    lst1, lst2 = [], []
    with open('d1_input.txt', 'r') as f:
        for line in f:
            split = line.split()
            lst1.append(int(split[0]))
            lst2.append(int(split[1]))

    # dont forgor to sort
    lst1.sort()
    lst2.sort()

    dif = 0
    for v1, v2 in zip(lst1, lst2):
        dif += abs(v1 - v2)

    return dif

def solution_2():
    lst1, lst2 = [], {}
    with open('d1_input.txt', 'r') as f:
        for line in f:
            split = line.split()
            lst1.append(int(split[0]))
            v2 = int(split[1])
            if v2 in lst2:
                lst2[v2] = lst2[v2]+1
            else:
                lst2[v2] = 1

    sim = 0
    for v1 in lst1:
        if v1 in lst2:
            sim += v1 * lst2[v1]

    return sim

def main():
    print(solution_1())
    print(solution_2())

if __name__ == '__main__':
    main()