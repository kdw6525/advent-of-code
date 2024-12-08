# https://adventofcode.com/2024/day/4
#
#
# Simple approach is to simply look for x's and go from there
# Making a graph would be fun thoooooo, so im doing it
#
from torch.cuda import graph


class Node:
    def __init__(self, v, row, col):
        # visual for the sake of me brain
        # 0 1 2
        # 3 X 4
        # 5 6 7
        # Direction matters so index will signal direction
        self.n = []
        # value in node
        self.v = v
        # row col you can find node
        self.row = row
        self.col = col

def make_neighbors(row, col):
    n = [None] * 8
    n[0] = (row-1, col-1)
    n[1] = (row-1, col)
    n[2] = (row-1, col+1)
    n[3] = (row, col-1)
    n[4] = (row, col+1)
    n[5] = (row+1, col-1)
    n[6] = (row+1, col)
    n[7] = (row+1, col+1)
    return n

def make_ws_graph(f):
    # :)
    # node keys are their coordinate position, aka (row, col)
    # direction of neighbor matters!!!!
    ws_graph = {}
    # making list of x's for solution 1
    x_s = []
    # making list of a's for solution 2
    a_s = []
    ws = [line for line in f]
    max_row = len(ws[0])
    for row in range(len(ws)):
        for col in range(max_row):
            # make node, put in dictionary
            node = Node(ws[row][col], row, col)
            node.n = make_neighbors(row, col)
            ws_graph[(row,col)] = node
            if node.v == 'X':
                x_s.append(node)
            elif node.v == 'A':
                a_s.append(node)


    return ws_graph, ws, x_s, a_s

def word_direction(ws_graph, node, word, d):
    # check if word exists in direction
    if node.v == word:
        return True
    elif node.v == word[0]:
        if node.n[d] in ws_graph:
            return word_direction(ws_graph, ws_graph[node.n[d]], word[1:], d)
    return False

def solution_1(ws_graph, x_s):
    count = 0
    for x in x_s:
        # since we have list of X nodes, we can look at neighbors
        for i in range(len(x.n)):
            if word_direction(ws_graph, x, 'XMAS', i):
                count += 1

    return count

def solution_2(ws_graph, a_s):
    count = 0
    # d1 is tl to br
    # d2 is bl to tr
    for a in a_s:
        # To count:
        # we need an MAS on both diagonals
        # these booleans tell if a diagonal is true
        # visual
        # tl . tr
        # .  A .
        # bl . br
        if a.n[0] in ws_graph:
            d1_node = ws_graph[a.n[0]]
            d1 = word_direction(ws_graph, d1_node, "MAS", 7) or word_direction(ws_graph, d1_node, "SAM", 7)
        else:
            d1 = False

        if a.n[2] in ws_graph:
            d2_node = ws_graph[a.n[2]]
            d2 = word_direction(ws_graph, d2_node, "MAS", 5) or word_direction(ws_graph, d2_node, "SAM", 5)
        else:
            d2 = False

        if d1 and d2:
            count += 1

    return count

def main():
    with open('d4_input.txt', 'r') as f:
        ws_graph, ws, x_s, a_s = make_ws_graph(f)

    print(solution_1(ws_graph, x_s))
    print(solution_2(ws_graph, a_s))

if __name__ == '__main__':
    main()