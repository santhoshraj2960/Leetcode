from collections import Counter, defaultdict


# ********** APPROACH 2 **********
"""
time O(N * W ^2)
space O(N)
"""
def get_longest_word_chain_2(words_list):
    words_set = set(words_list)
    memo = {}
    res = 0

    def dfs(word):
        nonlocal memo

        if word in memo: return memo[word]

        max_len_word_chain = 0

        for i in range(len(word)):
            new_word = word[:i] + word[i + 1:]

            if new_word in words_set:
                max_len_word_chain = max(max_len_word_chain, dfs(new_word))

        memo[word] = 1 + max_len_word_chain
        return memo[word]

    for word in words_list:
        res = max(dfs(word), res)

    return res

print(get_longest_word_chain_2(["a","b","ba","bca","bda","bdca"]))
print(get_longest_word_chain_2(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
print(get_longest_word_chain_2(["abcd","dbqca"]))



# ********* APPROACH 2 *************
"""
time O(N ^ 2)
space O(N)
"""
def get_longest_word_chain(words_list):
    predes_dict = defaultdict(set)

    # ********************* READ the definition of predes from question properly **********
    """wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA 
    without changing the order of the other characters to make it equal to wordB"""
    def check_if_word_1_pred_word_2_WRONG(w1, w2):
        if abs(len(w1) - len(w2)) != 1:
            return False

        w1_counter = Counter(w1)

        for ch in w2:
            if ch in w1_counter:
                w1_counter[ch] -= 1
                if w1_counter[ch] == 0:
                    w1_counter.pop(ch)

        if len(w1_counter.items()) == 1 and list(w1_counter.items())[0][1] == 1:
            return True

    def check_if_word_1_pred_word_2(w1, w2):  # xbc cxbc
        """
        In order for w1 to be predes of w2, len of w1 should be strictly less than len of w2 by 1. w2 should have
        only 1 additional character than w1 and the ordering of remaining chars should be same
        :param w1:
        :param w2:
        :return:
        """
        if not len(w2) - len(w1) == 1:
            return False

        num_diffs = 0
        i = j = 0
        # len of w1 is < len w2
        while i < len(w1) or j < len(w2):
            if num_diffs > 1: return False
            if i >= len(w1):
                j += 1
                num_diffs += 1
                continue

            if w1[i] == w2[j]:
                i += 1
                j += 1

            else:
                j += 1
                num_diffs += 1

        return num_diffs == 1

    for i in range(len(words_list)):
        for j in range(len(words_list)):
            word_1 = words_list[i]
            word_2 = words_list[j]

            if check_if_word_1_pred_word_2(word_1, word_2):
                predes_dict[word_2].add(word_1)

    memo = {}

    def dfs(word):
        nonlocal memo

        if not predes_dict[word]: return 1

        if word in memo: return memo[word]

        max_len_word_chain = 0

        for pred in predes_dict[word]:
            max_len_word_chain = max(max_len_word_chain, dfs(pred))

        memo[word] = 1 + max_len_word_chain
        return memo[word]

    res = 0

    for word in words_list:
        res = max(res, dfs(word))

    return res


"""
print(get_longest_word_chain(["a","b","ba","bca","bda","bdca"]))
print(get_longest_word_chain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
print(get_longest_word_chain(["abcd","dbqca"]))
"""