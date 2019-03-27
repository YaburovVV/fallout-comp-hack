import numpy as np


class WordListStats:
    def __init__(self, wordList):
        self.wordList = wordList
        self.wordTree = {}
        self.gen_tree()
        self.wordCountGroups = {}
        self.gen_count_groups()

    def gen_tree(self):
        for x in self.wordList:
            self.wordTree[x] = {}
            a = {}
            for y in self.wordList:
                if x != y:
                    a.update({y: self.calc_com_let(x, y)})
            self.wordTree[x] = [(k, a[k]) for k in sorted(a, key=a.get, reverse=True)]

    def print_tree(self):
        print_tree(self.wordTree)
        print_______()

    def print_count_groups(self):
        print_tree2(self.wordCountGroups)
        print_______()

    def gen_count_groups(self, print_output=False):
        for root_word in self.wordTree:
            column = self.wordTree[root_word]
            self.wordCountGroups[root_word] = {}
            for sub_group in column:
                self.wordCountGroups[root_word][sub_group[1]] = []
            for sub_group in column:
                self.wordCountGroups[root_word][sub_group[1]].append(sub_group[0])
        if print_output:
            print_tree2(self.wordCountGroups)

    @staticmethod
    def calc_com_let(firstWord, secondWord):
        count = 0
        for index, value in enumerate(firstWord):
            if firstWord[index] == secondWord[index]:
                count += 1
        return count

    def find_words(self, word, count, print_output=False):
        selected = []
        for cur in self.wordList:
            if self.calc_com_let(cur, word) == count:
                selected.append(cur)
        if print_output:
            print_list(selected, word + ' (' + str(count) + ') --> ')
        return selected

    def find_candidates(self, print_output=False):
        if print_output:
            print('# tree')
            self.print_tree()
            print('---------------')

        matches_count = {}
        for x in self.wordTree:
            stat0 = [x[1] for x in self.wordTree[x]]
            un = np.unique(stat0)
            matches_count[x] = []
            for y in un:
                matches_count[x].append((y, stat0.count(y)))
        if print_output:
            print('# matches_count')
            print_tree(matches_count)
            print('---------------')

        max_counts = {}
        for x in matches_count:
            max_counts[x] = [(max(matches_count[x], key=lambda x: x[1]))]
        if print_output:
            print('# max_counts - maximums in groups')
            print_tree(max_counts)
            print('---------------')

        min_maxs = [(x, max_counts[x][0][1]) for x in max_counts]
        min_value = min(min_maxs, key=lambda x: x[1])[1]
        if print_output:
            print('# min_maxs - minimums from maximums')
            print_list(min_maxs)
            print('min_value', min_value)
            print('---------------')

        stat4 = [x[0] for x in min_maxs if x[1] == min_value]

        return stat4


def print_tree2(tree_dic):
    for x in tree_dic:
        print(x)
        print_tree(tree_dic[x], '  ⋅')


def print_tree(tree_dic, ident=''):
    for x in tree_dic:
        print(ident, x)
        print_list(tree_dic[x], '\t' + ident)


def print_list(list_dic, ident=''):
    for cur in list_dic:
        print(ident, cur)


def print_list_num(list_dic):
    num = 1
    for cur in list_dic:
        print(str(num) + ')', cur)
        num += 1


def print_______():
    print('___________________')
