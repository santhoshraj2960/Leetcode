'''

Not sure why my folution (the following) fails for a few test cases.. But have a look at the trie solution stated in the
below link
https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/discuss/1676859/Trie-vs.-Bitmask-vs.-Sorting

target_dict = {
            'tack':
                {'t':1, 'a':1, c:1, k:1},
                }
source_dict = {
                'act':
                    {'a':1, 'c':1, 't':1}
}
for word in source: O(w)
    for chars a to z: O(1)
        chars_dict_word = source_dict[word]
        append char to chars_dict_word if char not in chars_dict_word O(1)
        if the modified dictionary in target => res + 1 O(t)
        else pop char

The following approaches won't work:
1) Trie: Because ordering of the characters in word do not matter (the letters can be in any arbitrary order)
2) Removing a char at the end of target word won't work: Read the conversion operation carefully!! You should append a character at the end of source word (it actually doesn't matter where you append it) and then rearrange the letterss

Final thoughts
1) You can use a trie if you sort the characters as mentioned in the link above
2) It's true that Removing a char at the end of target word won't work: But removing one character at a time from the sorted_word in the target and checking if it is in the sorted_source_words_set (where the characters in each word are sorted) will word

Understand bitmask by analysing the following python terminal output
def mask(ch):
    return 1 << ord(ch) - ord('a') # Left shifting by 1 bit => 2^0 will become 2^1 || 2^1 will become 2^2 and so on

mask('a') # binary representaion 1
1
mask('b')# binary representaion  1 0
2
mask('b') + mask('a') # binary representaion 1 1
3

res = 0

source = 'abcd'
target = 'abcds'

res = sum(mask(ch) for ch in source)
print(res) => 15

res_t = sum(mask(ch) for ch in target)
print(res_t) => 262159

res_t = sum(mask(ch) for ch in target[:-1])
print(res_t) => 15
'''
from collections import defaultdict


class Solution:
    def wordCount(self, source_words, target_words):
        def get_char_mask(char):
            return 1 << ord(char) - ord('a')

        def get_bit_mask_word(word):
            return sum(get_char_mask(ch) for ch in word)

        source_word_bitmap_set = set()
        res = 0

        for word in source_words:
            source_word_bitmap_set.add(get_bit_mask_word(word))

        # print(source_word_bitmap_set)

        for word in target_words:
            target_word_bit_mask = get_bit_mask_word(word)
            for ch in word:
                bitmask_of_word_without_ch = target_word_bit_mask - get_char_mask(ch)

                if bitmask_of_word_without_ch in source_word_bitmap_set:
                    res += 1
                    break

        return res

        """
        result_set = set()

        def frame_dict_from_words(words_list):
            word_char_map = defaultdict(dict)
            for word in words_list:
                for char in word: 
                    if char in word_char_map[word]: word_char_map[word][char] += 1
                    else: word_char_map[word][char] = 1

            return word_char_map

        def check_if_present_in_target(source_word_dict):
            for target_word in target_words_dict:
                if target_word in result_set: continue
                if target_words_dict[target_word] == source_word_dict:
                    result_set.add(target_word)
                    return True

            return False


        source_words_dict = frame_dict_from_words(startWords)
        target_words_dict = frame_dict_from_words(targetWords)
        # print(source_words_dict)
        # print(target_words_dict)
        res = 0

        for word in startWords:
            word_chars_map = source_words_dict[word]
            for ascii_char in range(97, 123):
                char = chr(ascii_char)
                if char not in word_chars_map:
                    word_chars_map[char] = 1
                    if check_if_present_in_target(word_chars_map): 
                        #print(word)
                        res += 1
                    word_chars_map.pop(char)

        return res
        """

