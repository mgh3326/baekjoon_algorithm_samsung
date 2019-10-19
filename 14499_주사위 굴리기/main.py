import sys

sys.stdin = open("input.txt")


def rotate(_idx):
    if _idx == 0:  # 동쪽
        dice_dict["east"], dice_dict["up"], dice_dict["west"], dice_dict["bottom"] = dice_dict["up"], dice_dict[
            "west"], dice_dict["bottom"], dice_dict["east"]
    elif _idx == 1:  # 서쪽
        dice_dict["east"], dice_dict["up"], dice_dict["west"], dice_dict["bottom"] = dice_dict["bottom"], dice_dict[
            "east"], dice_dict["up"], dice_dict["west"]
    elif _idx == 2:  # 북쪽
        dice_dict["up"], dice_dict["front"], dice_dict["bottom"], dice_dict["back"] = dice_dict["front"], dice_dict[
            "bottom"], dice_dict["back"], dice_dict["up"]
    elif _idx == 3:  # 남쪽
        dice_dict["up"], dice_dict["front"], dice_dict["bottom"], dice_dict["back"] = dice_dict["back"], dice_dict[
            "up"], dice_dict["front"], dice_dict["bottom"]


dice_dict = {
    "up": 0,
    "back": 0,
    "east": 0,
    "west": 0,
    "front": 0,
    "bottom": 0,
}
dice_list = [0] * 6
dir_list = [
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
]
N, M, h, w, K = map(int, input().split())
board_list = [list(map(int, input().split())) for i in range(N)]

result = 0
d_list = list(map(int, input().split()))
for _d in d_list:
    d = _d - 1
    dh, dw = dir_list[d]
    nh, nw = h + dh, w + dw
    if nh < 0 or nw < 0 or nh >= N or nw >= M:
        continue
    h, w = nh, nw
    # rotate
    rotate(d)
    print(dice_dict["up"])
    if board_list[nh][nw] != 0:
        dice_dict["bottom"] = board_list[nh][nw]
        board_list[nh][nw] = 0
    else:
        board_list[nh][nw] = dice_dict["bottom"]
