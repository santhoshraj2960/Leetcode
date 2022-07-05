# https://leetcode.com/problems/find-and-replace-in-string/

# time: O(k + n)) || k is the len of indices and n is the len of s
def find_and_replace_string(s, indices, source, target):
    indices_source_target = {}  # {0 : [‘ab’, ‘eee’], 2: [‘cd’, ‘ffff’]}

    for i in range(len(indices)):
        indices_source_target[indices[i]] = [source[i], target[i]]

    i = 0
    res = []
    while i < len(s):
        if i in indices_source_target:
            src = indices_source_target[i][0]
            target = indices_source_target[i][1]
            len_of_replacement_str = len(src)
            input_substring = ''
            src_in_input_at_index = True
            j = 0

            while j < len_of_replacement_str and i < len(s):
                if s[i] != src[j]:
                    src_in_input_at_index = False

                input_substring += s[i]
                i += 1
                j += 1

            if src_in_input_at_index and j == len_of_replacement_str:
                res.append(target)
            else:
                res.append(input_substring)
        else:
            res.append(s[i])
            i += 1

    return ''.join(res)


print(find_and_replace_string('abcd', [0, 2], ['ab', 'cd'], ["eee", "ffff"]))
print(find_and_replace_string('abcdxy', [0, 2], ['ab', 'cd'], ["eee", "ffff"]))
print(find_and_replace_string('abxycd', [0, 2], ['ab', 'cd'], ["eee", "ffff"]))
print(find_and_replace_string('abxycd', [0, 4], ['ab', 'cd'], ["eee", "ffff"]))
print(find_and_replace_string('abxycr', [0, 4], ['ab', 'cd'], ["eee", "ffff"]))
print(find_and_replace_string('abxycr', [0, 4], ['ab', 'cde'], ["eee", "ffff"]))
