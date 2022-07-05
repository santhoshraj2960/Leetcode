from collections import deque


class Solution:
    def fullJustify(self, words: [str], max_width: int) -> [str]:

        def distribute_words_in_line(words):  # [This, is, an] || max_width = 16
            # print('words = ', words)
            if len(words) == 1: return words[0] + (' ' * (max_width - len(words[0])))

            num_blanks_to_insert_empty_strings = len(words) - 1  # 2
            space_needed_for_words = 0
            for word in words: space_needed_for_words += len(word)  # 8
            rem_width = max_width - space_needed_for_words  # 16 - 8 = 8
            evenly_distributed_spaces, additional_spaces = divmod(rem_width, num_blanks_to_insert_empty_strings)

            line = []

            for word in words[:-1]:
                line.append(word)
                line.append(' ' * evenly_distributed_spaces)
                if additional_spaces > 0:
                    line.append(' ')
                    additional_spaces -= 1

            line.append(words[-1])
            return ''.join(line)

        words = deque(words)
        res = []

        while words:

            space_left_in_current_line = max_width  # 16
            words_in_line = []

            while words and space_left_in_current_line - len(
                    words[0]) >= 0:  # 16 - 4 > 0 || 11 - 2 > 0 || 8 - 2 > 0 || 5 - 6 > 0 (F)
                word_to_be_added_to_line = words.popleft()  # This || is || an
                words_in_line.append(word_to_be_added_to_line)  # [This, is, an
                space_left_in_current_line -= (len(word_to_be_added_to_line) + 1)  # 11 || 8 || 5

            if words:
                res.append(distribute_words_in_line(words_in_line))  # [This, is, an]
            else:
                last_line = []
                for word in words_in_line:
                    last_line.append(word)
                    max_width -= len(word)
                    if max_width > 0: last_line.append(' ')
                    max_width -= 1

                last_line.append(' ' * max_width)
                res.append(''.join(last_line))

        return res
