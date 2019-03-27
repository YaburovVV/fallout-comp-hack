import numpy as np


class WordListStats:
    def __init__(self, wordList):
        self.wordList = wordList

    @staticmethod
    def calc_com_let(firstWord, secondWord):
        count = 0
        for index, value in enumerate(firstWord):
            if firstWord[index] == secondWord[index]:
                count += 1
        return count

    def find_words(self, word, count, print_output=False):
        list = []
        for cur in self.wordList:
            if self.calc_com_let(cur, word) == count:
                list.append(cur)
        if print_output:
            print_list(list, word + ' (' + str(count) + ') --> ')
        return list

    def find_candidates(self, print_output=False):
        tree = {}
        for x in self.wordList:
            tree[x] = {}
            a = {}
            for y in self.wordList:
                if x != y:
                    a.update({y: self.calc_com_let(x, y)})
            tree[x] = [(k, a[k]) for k in sorted(a, key=a.get, reverse=True)]
        if print_output:
            print('tree')
            print_tree(tree)
            print('---------------')

        stat = {}
        for x in tree:
            stat0 = [x[1] for x in tree[x]]
            un = np.unique(stat0)
            stat[x] = []
            for y in un:
                stat[x].append((y, stat0.count(y)))
        if print_output:
            print('stat1')
            print_tree(stat)
            print('---------------')

        stat2 = {}
        for x in stat:
            stat2[x] = [(max(stat[x], key=lambda x: x[1]))]
        if print_output:
            print('stat2 - maximums in groups')
            print_tree(stat2)
            print('---------------')

        stat3 = [(x, stat2[x][0][1]) for x in stat2]
        min_value = min(stat3, key=lambda x: x[1])[1]
        if print_output:
            print('stat3 - minimums from maximums')
            print_list(stat3)
            print('min_value', min_value)
            print('---------------')

        stat4 = [x[0] for x in stat3 if x[1] == min_value]

        return stat4


def print_tree(tree_dic):
    for x in tree_dic:
        print(x)
        print_list(tree_dic[x], '\t')


def print_list(list_dic, ident=''):
    for cur in list_dic:
        print(ident, cur)
