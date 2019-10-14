import sys

sys.stdin = open("./data/input1.txt", "r")
import itertools

test_case_num = int(input())
for test_case_index in range(test_case_num):
    chapter_size = int(input())
    temp_list = []
    for i in range(chapter_size):
        temp_list.append(i)
    chapter_list = list(map(int, input().split()))
    combinations = list(itertools.combinations(temp_list, 2))
    for combination in combinations:
        current_list = []
        for temp in temp_list:
            if temp not in combination:
                current_list.append(temp)
        oh = list(itertools.combinations(current_list, 2))
        print()

        print()
    print()
