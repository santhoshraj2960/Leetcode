"""
10:19 - 10:44

ant [a-z] => antb (sort)=> abnt => target_words_set.pop(sorted_sourceword)
abt [a-z] => abtn (sort)=> abnt

num_of_target_words = t
max_len_target_word = n

num_of_source_words = s
max_len_target_word = m

time: (t* n log n) + (s * m log m)
space: O(t*n) + O(m)

"""

from collections import defaultdict
class Solution:
    def wordCount(self, start_words, target_words) -> int:
        # target_words_set = set()  # set(["act"])
        target_words_dict = defaultdict(int)
        res = 0  # 2

        for word in target_words:
            letters = [ch for ch in word]
            letters.sort()
            # target_words_set.add(''.join(letters))
            target_words_dict[''.join(letters)] += 1

        for word in start_words:  # ant

            chars_list = [ch for ch in word]  # [a, c, t]
            chars_set = set(chars_list)  # set([a,c,t])

            for ascii_i in range(97, 123):  # [a - z]
                if chr(ascii_i) in chars_set: continue  # a, c, t

                chars_list.append(chr(ascii_i))  # [a,c,t]
                chars_list.sort()  # [a,c,t]
                transformed_word = ''.join(chars_list)  # act

                if transformed_word in target_words_dict:
                    res += target_words_dict[transformed_word]
                    target_words_dict.pop(transformed_word)
                    # target_words_set.remove(transformed_word)
                    """
                    target_words_dict[transformed_word] -= 1 # source = ['u'] target = ['mu', 'mu']
                    if target_words_dict[transformed_word] == 0: target_words_dict.pop(transformed_word)
                    """

                chars_list.remove(chr(ascii_i))

        return ret_val, res

"""
Points to note:
1) target can have duplicates (SO, using a set to store target words will count the same target word occuring multiple times, as a ONE word). 
    - DON'T use set to store target words. Plus, two different unsorted words may become equal after sorting. 
    - eg: target = ['ab','ba'] (sort letters in each word)=> [ab, ab] 
        set(['ab', 'ab']) => set(['ab']) 
        set(['ab', 'ba]) => set(['ab, 'ba'])

    - Using dict for the same example stated above
        target_dict = {'ab':2}

2) testcase => source = ['b'] target = ['ab', 'ab'] || output should be 2 coz target words first 'ab' and second 'ab' can be formed by performing 
'conversion operation' on the single 'b' that is present in source. This is why I commented the block starting at "target_words_dict[transformed_word] -= 1"
"""