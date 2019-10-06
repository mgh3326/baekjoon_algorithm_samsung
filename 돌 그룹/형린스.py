import sys
from collections import deque

# 돌은 A,B,C개의 세 그룹으로 나누어짐

base_groups = list(map(int, sys.stdin.readline().split()))
stack = deque([tuple(sorted(base_groups))])
visited = set(tuple(sorted(base_groups)))

is_ok = False
while stack:
    groups = stack.pop()

    if groups[0] == groups[1] and groups[1] == groups[2]:
        is_ok = True
        break

    # 크기가 같지 않은 두 그룹 선택
    for g1, g2, rest_g in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]:
        if groups[g1] == groups[g2]:  # 같으면 안돼
            continue
        # 작은쪽 X, 큰 쪽 Y라 하고
        X = groups[g1] if groups[g1] < groups[g2] else groups[g2]
        Y = groups[g1] if groups[g1] > groups[g2] else groups[g2]

        # X = X+X, Y = Y-X
        new_groups = tuple(sorted([X + X, Y - X, groups[rest_g]]))
        if new_groups[0] == new_groups[1] and new_groups[1] == new_groups[2]:
            is_ok = True
            break

        if not new_groups in visited:
            stack.append(tuple(new_groups))
            visited.add(tuple(new_groups))

    if is_ok == True:
        break

# A,B,C 모두 같은 개수 만들수 있으면 1, 아니면 0
if is_ok == True:
    print(1)
else:
    print(0)
