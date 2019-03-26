#!/usr/bin/env python3
import numpy as np

wordList = []
with open('list.txt', 'r') as f:
    wordList = f.readlines()
f.close()

wordList = [x.replace('\n', '') for x in wordList]


def count_common_number(first, second):
    count = 0
    for index, value in enumerate(first):
        if first[index] == second[index]:
            count += 1
    return count


def print_tree(tree_dic):
    for x in tree_dic:
        print(x)
        for y in tree_dic[x]:
            print('\t', y)


tree = {}

for x in wordList:
    tree[x] = {}
    a = {}
    for y in wordList:
        if x != y:
            a.update({y: count_common_number(x, y)})
    tree[x] = [(k, a[k]) for k in sorted(a, key=a.get, reverse=True)]

print('tree')
# print_tree(tree)
print('---------------')
stat = {}

for x in tree:
    stat0 = [x[1] for x in tree[x]]
    un = np.unique(stat0)
    stat[x] = []
    for y in un:
        stat[x].append((y, stat0.count(y)))

print('stat1')
# print_tree(stat)
print('---------------')


stat2 = {}
for x in stat:
    stat2[x] = [(max(stat[x], key=lambda x: x[1]))]

print('stat2')
# print_tree(stat2)
print('---------------')

stat3 = [(x, stat2[x][0][1]) for x in stat2]
min_value = min(stat3, key=lambda x: x[1])[1]
# print('stat3', stat3)
# print('min_value', min_value)
print('---------------')

print('Words for choosing')
stat4 = [x[0] for x in stat3 if x[1] == min_value]
print('stat4', stat4)
print('---------------')

for x in stat4:
    branch = {x: tree[x]}
    # print_tree(branch)

    branch_vv = {}
    for y in branch[x]:
        branch_vv[(x, y[1])] = []
    for y in branch[x]:
        branch_vv[(x, y[1])].append(y[0])

    for y in branch_vv:
        print(y, branch_vv[y])
    print('---------------')

    for y in branch_vv:
        br_arr = branch_vv[y]
        if len(br_arr) > 1:
            print('')
            print('==', y, '==')

            sub_tree_sorted = {}
            for a in br_arr:
                sub_tree_sorted[a] = []
                temp = {}
                for b in br_arr:
                    if a != b:
                        temp.update({b: count_common_number(a, b)})
                sub_tree_sorted[a] = [(k, temp[k]) for k in sorted(temp, key=temp.get, reverse=True)]

            print_tree(sub_tree_sorted)
            print('---------------')



