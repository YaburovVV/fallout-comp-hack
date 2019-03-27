#!/usr/bin/env python3
from wordListStats import *

wordList = []
with open('list.txt', 'r') as f:
    wordList = f.readlines()
f.close()

wordList = [x.replace('\n', '') for x in wordList]
wls = WordListStats(wordList)
wls.print_count_groups()

print("Choose word: ")
cands = wls.find_candidates()
print_list_num(cands)
num = input("Variant ")
selected_word = cands[int(num)-1]
print('-->', selected_word)
group = wls.wordCountGroups[selected_word]
print_tree(group)
num = input("Count matches ")

wls = WordListStats(group[int(num)])
# wls.print_tree()
wls.print_count_groups()
cands = wls.find_candidates()
print_list_num(cands)
num = input("Variant ")
selected_word = cands[int(num)-1]
print('-->', selected_word)
group = wls.wordCountGroups[selected_word]
print_tree(group)
num = input("Count matches ")

wls = WordListStats(group[int(num)])
# wls.print_tree()
wls.print_count_groups()
cands = wls.find_candidates()
print_list_num(cands)
num = input("Variant ")
selected_word = cands[int(num)-1]
print('-->', selected_word)
group = wls.wordCountGroups[selected_word]
print_tree(group)
num = input("Count matches ")

