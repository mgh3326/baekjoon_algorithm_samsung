import sys

sys.stdin = open("input.txt")
# (해결) 대칭을 빼먹어서 틀려버림
dirs_list = [
    [(0, 1), (0, 2), (0, 3)],  # 1번
    [(1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1)],  # 2번
    [(1, 0), (2, 0), (2, 1)],  # 3번
    [(1, 0), (2, 0), (2, -1)],
    [(0, 1), (0, 2), (1, 0)],
    [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(0, 1), (0, 2), (1, 2)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 1), (1, 0), (2, 0)],

    [(1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 0), (-1, 1)],
    [(0, 1), (1, 0), (1, -1)],
    [(0, 1), (1, 1), (1, 2)],

    [(0, 1), (0, 2), (1, 1)],
    [(1, 0), (1, 1), (1, -1)],
    [(1, 0), (2, 0), (1, -1)],
    [(1, 0), (1, 1), (2, 0)]
]
# dirs_list = [
#     [[0, 1], [0, 2], [0, 3], ],  # 1번
#     [[1, 0], [2, 0], [3, 0], ],
#     [[0, 1], [1, 0], [1, 1], ],  # 2번
#     [[1, 0], [2, 0], [2, 1], ],  # 3번
#     [[1, 0], [2, 0], [0, 1], ],
#     [[0, 1], [0, 2], [1, 0], ],
#     [[0, 1], [0, 2], [-1, 0], ],
#
#     [[0, 1], [1, 1], [2, 1], ],
#     [[0, 1], [-1, 1], [-2, 1], ],
#
#     [[0, 1], [0, 2], [-1, 2], ],
#     [[0, 1], [0, 2], [1, 2], ],
#
#     [[1, 0], [1, 1], [2, 1], ],  # 4번
#     [[1, 0], [1, 0], [-1, 1], ],
#
#     [[0, 1], [-1, 1], [-1, 2], ],
#     [[0, 1], [1, 1], [1, 2], ],
#
#     [[0, 1], [1, 1], [0, 2], ],  # 5번
#     [[1, 0], [1, 1], [2, 0], ],
#     [[0, 1], [-1, 1], [0, 2], ],
#     [[0, 1], [-1, 1], [1, 1], ],
# ]
N, M = map(int, input().split())
board_list = [(list(map(int, input().split()))) for i in range(N)]
result = 0
for h in range(N):
    for w in range(M):
        for dirs in dirs_list:
            current_value = board_list[h][w]
            for dh, dw in dirs:
                nh, nw = h + dh, w + dw
                if nh < 0 or nw < 0 or nh >= N or nw >= M:
                    break
                current_value += board_list[nh][nw]
            else:
                if result < current_value:
                    result = current_value
print(result)
