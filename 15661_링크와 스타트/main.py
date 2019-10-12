import sys

sys.stdin = open("./data/input1.txt", "r")

import itertools

result = -1
people_num = int(input())
index_list = []
score_dict = {}
for i in range(people_num):
    index_list.append(i)
people_list = []
for i in range(people_num):
    people_list.append(list(map(int, input().split())))
for i in range(people_num - 2):
    if result==0:
        break
    combinations = list(itertools.combinations(index_list, i + 2))
    for combination in combinations:
        if combination not in score_dict:
            oh_list = list(itertools.combinations(combination, 2))
            score = 0
            for oh in oh_list:
                score += people_list[oh[0]][oh[1]] + people_list[oh[1]][oh[0]]
            score_dict[combination] = score
        link_list = []
        for index in index_list:
            if index not in combination:
                link_list.append(index)
        link_list = tuple(link_list)
        if link_list not in score_dict:
            oh_list = list(itertools.combinations(link_list, 2))
            score = 0
            for oh in oh_list:
                score += people_list[oh[0]][oh[1]] + people_list[oh[1]][oh[0]]
            score_dict[link_list] = score

        abs1 = abs(score_dict[combination] - score_dict[link_list])
        if result == -1 or abs1 < result:
            result = abs1
            if result==0:
                break

print(result)
