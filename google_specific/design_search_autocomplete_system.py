"""
Refer the following sols as well
    - https://leetcode.com/problems/design-search-autocomplete-system/discuss/105386/Python-Clean-Solution-Using-Trie
"""
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.next = {}
        self.word_end_occurances = 0


class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.trie_root = TrieNode('root')

        for i, sentance in enumerate(sentences):
            self.add_user_input_to_trie(sentance, times[i])

        self.current_user_inp = []

    def add_user_input_to_trie(self, sentance, num_times, caller_input=False):
        parent_trie_node = self.trie_root
        for character in sentance:
            if character in parent_trie_node.next:
                curr_trie_node = parent_trie_node.next[character]
            else:
                curr_trie_node = TrieNode(character)
                parent_trie_node.next[character] = curr_trie_node

            parent_trie_node = curr_trie_node

        if caller_input == False:
            parent_trie_node.word_end_occurances = num_times
        else:
            # print('\n', parent_trie_node.word_end_occurances)
            parent_trie_node.word_end_occurances += 1
            # print(parent_trie_node.word_end_occurances)

    def input(self, c: str):
        self.current_user_inp.append(c)
        curr_user_inp = ''.join(self.current_user_inp)
        res = []
        path = []
        i = 0

        if curr_user_inp[-1] == '#':
            self.add_user_input_to_trie(curr_user_inp[:-1], 1, caller_input=True)
            self.current_user_inp = []
            return []

        parent_trie_node = self.trie_root

        while i < len(curr_user_inp) and curr_user_inp[i] in parent_trie_node.next:
            parent_trie_node = parent_trie_node.next[curr_user_inp[i]]
            path.append(curr_user_inp[i])
            i += 1

        def get_all_possible_paths(parent_trie_node):
            nonlocal res

            # Note: don't return from inside if: if you have added the following words into your trie, "a", "abc", "abd", then the user types "a", you should recommend all the words added to your trie. see the example testcase that failed (in submissions tab)
            if parent_trie_node.word_end_occurances != 0:
                res.append((parent_trie_node.word_end_occurances, ''.join(list(path))))

            for next_char in parent_trie_node.next:
                path.append(next_char)
                get_all_possible_paths(parent_trie_node.next[next_char])
                path.pop()

        if i == len(curr_user_inp):
            get_all_possible_paths(parent_trie_node)

            # Note: you first sort by num of occurances (in descending). Then sort (in ascending) by the actual word itself "i love l" is less than "ironman". this is the example input given
            res.sort(key=lambda x: (-x[0], x[1]))
            # print(res, '\n')
            res = res[:3]
            return_val = [tup[1] for tup in res]
            return return_val

        else:
            return []


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
"""
["AutocompleteSystem","input","input","input","input","input","input","input","input","input","input","input","input","input","input"]
[[["abc","abbc","a"],[3,3,3]],["b"],["c"],["#"],["b"],["c"],["#"],["a"],["b"],["c"],["#"],["a"],["b"],["c"],["#"]]
"""
sentences = ["abc","abbc","a"]
times = [3,3,3]
a = AutocompleteSystem(sentences, times)
c = 'a'
print(a.input(c))
"""c = ' '
print(a.input(c))
c = 'a'
print(a.input(c))
c = '#'
print(a.input(c))"""