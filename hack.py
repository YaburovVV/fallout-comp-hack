#!/usr/bin/env python3
from wordListStats import *

wordList = []
with open('list.txt', 'r') as f:
    wordList = f.readlines()
f.close()

wordList = [x.replace('\n', '') for x in wordList]
wls = WordListStats(wordList)
cands = wls.find_candidates(True)

words = wls.find_words(cands[0], 2, True)


# cands_l1 = find_candidates(wordList)
# print('Words for choosing')
# print(cands_l1)
# for x in stat4:
#     branch = {x: tree[x]}
#     # print_tree(branch)
#
#     branch_vv = {}
#     for y in branch[x]:
#         branch_vv[(x, y[1])] = []
#     for y in branch[x]:
#         branch_vv[(x, y[1])].append(y[0])
#
#     for y in branch_vv:
#         print(y, branch_vv[y])
#     print('---------------')
#
#     for y in branch_vv:
#         br_arr = branch_vv[y]
#         if len(br_arr) > 1:
#             print('')
#             print('==', y, '==')
#
#             sub_tree_sorted = {}
#             for a in br_arr:
#                 sub_tree_sorted[a] = []
#                 temp = {}
#                 for b in br_arr:
#                     if a != b:
#                         temp.update({b: count_common_number(a, b)})
#                 sub_tree_sorted[a] = [(k, temp[k]) for k in sorted(temp, key=temp.get, reverse=True)]
#
#             print_tree(sub_tree_sorted)
#             print('---------------')
