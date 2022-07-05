"""
word_index = 0
len(word) + 1 is the space (remaining col) needed in the row to fit the word
when word_index reaches len(sentence) => res = res + 1 and word_indx = 0

Refer
    - https://leetcode.com/problems/sentence-screen-fitting/discuss/90869/Python-with-explanation
    - https://leetcode.com/problems/sentence-screen-fitting/discuss/90845/21ms-18-lines-Java-solution
"""


class Solution:
    def wordsTyping(self, sentence, rows: int, cols: int) -> int:
        # Approach 1
        # Time: O(r * max_word_len)) r is the num of rows and max_word_lenis len of the longest word in sentence
        s = ' '.join(sentence) + ' '
        start = 0

        # h e l l o   w o r l d  ''
        # 0 1 2 3 4 5 6 7 8 9 10 11
        # a   b c d   e ''
        # 0 1 2 3 4 5 6  7
        for row in range(rows):  # O(r)
            start = start + cols

            if s[start % len(s)] == ' ':
                start += 1

            else:
                # cannot fit characters untill start position. Traverse back till you reach ' '
                while start > 0 and s[(start - 1) % len(s)] != ' ':  # O(max_word_len)
                    start -= 1

        return start // len(s)

        """
        Approach 2 - Time Limit Exceeded

        time: O(r * c) r is the num of rows and c is the num of cols

        word_index = 0
        res = 0

        for row in range(rows):
            remaining_cols = cols

            while remaining_cols >= len(sentence[word_index]):
                remaining_cols -= (len(sentence[word_index]) + 1)
                word_index += 1

                if word_index == len(sentence): word_index, res = 0, res + 1  

        return res
        """
