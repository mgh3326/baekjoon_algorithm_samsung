import sys

sys.stdin = open("./data/input1.txt", "r")

import math

test_room_number = int(input())
test_room_list = list(map(int, input().split()))
chong_num, boo_num = map(int, input().split())
result = test_room_number
for test_room in test_room_list:
    num = (test_room - chong_num) / boo_num
    if num<0:
        continue
    ceil = math.ceil(num)
    result += ceil
print(result)
