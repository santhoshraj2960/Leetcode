"""
At no point in the qus we are given that the indices list is sorted || indices = [3,5,1] is valid input

If you don't sort the indices and its corresponding sources and targets together, code will fail
eg test case:
"vmokgggqzp"
[3,5,1]
["kg","ggq","mo"]
["s","so","bfr"]
"""

# time: O(k log k + O(n)) || k is the len of indices and n is the len of s
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        zipped_inputs = list(zip(indices, sources, targets))
        zipped_inputs.sort()

        indices_ptr = 0
        s_ptr = 0
        res = []

        while s_ptr < len(s):
            if indices_ptr < len(zipped_inputs) and s_ptr == zipped_inputs[indices_ptr][0]:

                j = 0
                source_word = zipped_inputs[indices_ptr][1]
                replace = True
                input_str_substr = s[s_ptr: s_ptr + len(source_word)]

                while j < len(source_word):

                    if source_word[j] != s[s_ptr]:
                        replace = False

                    j += 1
                    s_ptr += 1

                if replace:
                    res.append(zipped_inputs[indices_ptr][2])
                else:
                    res.append(input_str_substr)

                indices_ptr += 1

            else:
                res.append(s[s_ptr])
                s_ptr += 1

        return ''.join(res)