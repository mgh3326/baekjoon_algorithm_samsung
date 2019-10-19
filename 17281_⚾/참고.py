import sys

sys.stdin = open("./data/input.txt")
import itertools
import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = 0
for it in itertools.permutations(range(1, 9), 8):
    new_it = list(it[:3]) + [0] + list(it[3:])
    index = 0
    score = 0
    for i in arr:
        out = 0
        one, two, three = 0, 0, 0

        while out < 3:
            if i[new_it[index]] == 0:
                out += 1
            elif i[new_it[index]] == 1:
                score += three
                one, two, three = 1, one, two
            elif i[new_it[index]] == 2:
                score += three + two
                one, two, three = 0, 1, one
            elif i[new_it[index]] == 3:
                score += three + two + one
                one, two, three = 0, 0, 1
            else:
                score += one + two + three + 1
                one, two, three = 0, 0, 0

            index = (index + 1) % 9
    result = max(result, score)
print(result)
