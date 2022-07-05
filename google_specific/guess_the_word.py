"""
All words have len of 6
definitely secret word is present

https://leetcode.com/problems/guess-the-word/discuss/160945/Python-O(n)-with-maximum-overlap-heuristic
"""


def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
    def get_max_overlap_word(words_list):
        ch_index_map = [{chr(i): 0 for i in range(97, 123)} for _ in range(6)]
        """
        [{'a': 2, 'c': 1, 'e': 1, ..}, 
        {'c': 3, 'i': 1},
        {},
        {},
        {},
        {}]
        """

        for word in words_list:
            for j, ch in enumerate(word):
                ch_index_map[j][ch] += 1

        max_word_score, max_word = 0, None

        for word in words_list:
            word_score = 0

            for i, ch in enumerate(word):
                word_score += ch_index_map[i][ch]

            if word_score > max_word_score:
                max_word_score, max_word = word_score, word

        return max_word

    def get_words_with_exactly_k_matches_to_word(words_list, prospective_key, k):
        words_with_k_matches = []

        for word in words_list:
            num_matches = 0
            for i, ch in enumerate(word):
                if ch == prospective_key[i]:
                    num_matches += 1

            if num_matches == k: words_with_k_matches.append(word)

        return words_with_k_matches

    while wordlist:
        prospective_key = get_max_overlap_word(wordlist)
        k = master.guess(prospective_key)

        if k == 6:
            return prospective_key

        else:
            wordlist = get_words_with_exactly_k_matches_to_word(wordlist, prospective_key, k)
