from collections import deque, defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: [str]) -> int:

        # approach 1 -> Linear time O(S * W) || S -> number of chars in s || W -> num of chars in all words
        # Have a look at the following solution. This uses iterator instead of deque to traverse each word
        # https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation
        matching_subsequences = 0
        word_first_char_map = defaultdict(list)

        for word in words:
            word_deque = deque([ch for ch in word[1:]])
            word_first_char_map[word[0]].append(word_deque)

        for char in s:
            if char not in word_first_char_map: continue

            all_corresponding_words = word_first_char_map[char]
            word_first_char_map.pop(char)

            for word_deque in all_corresponding_words:
                if not word_deque:
                    matching_subsequences += 1
                    continue

                first_char = word_deque.popleft()
                word_first_char_map[first_char].append(word_deque)

        return matching_subsequences

        """
        matching_subsequences = 0
        for word in words:
            if len(word) > len(s): continue
            word_ptr = 0
            source_ptr = 0

            while source_ptr < len(s) and word_ptr < len(word):
                if s[source_ptr] == word[word_ptr]:
                    word_ptr += 1

                source_ptr += 1

            if word_ptr == len(word): matching_subsequences += 1

        return matching_subsequences
        """

