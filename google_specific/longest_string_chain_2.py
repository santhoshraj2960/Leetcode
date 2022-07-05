"""
word_a prede of word_b if
    - insert exactly one letter anywhere in word_a

words_set = set of words

iterate each word
    iterate through each position in word
        {insert one character from a-z in that pos and check if it is in words_set} -> If yes -> recurse(or backtrasck)

word = 'abc'
i = 0
word[:0] + char + word[1:]

time: O(w * c ^ 2) w is the numof words and c is the max number of chars in an input word
"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_set = set(words)
        memo = {}

        def recurse(word):
            nonlocal memo

            if word in memo:
                return memo[word]

            max_word_chain_len_from_word = 1

            # range(len(words) + 1) => "+ 1" is used because you want to handle the following scenario
            # abc => abcd (you should insert 'd' at the end of the word and see if "abcd" is in words_set)
            for i in range(len(word) + 1):
                for ascii_val in range(97, 123):
                    char = chr(ascii_val)
                    new_word = word[:i] + char + word[i:]

                    if new_word in words_set:
                        len_of_curr_word_chain = 1 + recurse(new_word)
                        max_word_chain_len_from_word = max(max_word_chain_len_from_word, len_of_curr_word_chain)

            memo[word] = max_word_chain_len_from_word
            return memo[word]

        res = float('-inf')

        for word in words:
            max_word_chain_len = recurse(word)
            res = max(res, max_word_chain_len)

        return res
