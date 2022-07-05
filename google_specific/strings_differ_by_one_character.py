"""
abcd
aacd

input_set = set(["abcd","acbd", "aacd"])
word = abcd
    - for ch in range [a-z] poss
        - bbcd || cbcd || dbcd || ..
"""


class Solution:
    def differByOne(self, words: [str]) -> bool:
        # Approach 1: O(m * n)
        hashes = [0] * len(words)
        mod = 10 ** 11 + 7  # mod is used to avoid "Memory Limit exception" => see submissions tab

        for i, word in enumerate(words):
            for ch in word:
                hashes[i] = ((26 * hashes[i]) + (ord(ch) - ord('a'))) % mod

        # print(hashes)

        base = 1
        seen = set()
        for j in range(len(words[0]) - 1, -1, -1):
            for i, word in enumerate(words):
                # Note the use od ord('Z'). If you use ord('a') insted of ord('Z'), when you get an input like ["aba","aac"], code will fail
                # because (base * ...) will have no effect when ... equals '0'
                # ... will become 0 when character is 'a' coz ord('a') - ord('a') = 0
                word_hash_without_char = (hashes[i] - (base * (ord(word[j]) - ord('Z')))) % mod

                if word_hash_without_char in seen:
                    print(word)
                    print(j)
                    return True
                else:
                    seen.add(word_hash_without_char)

            base = 26 * base % mod
        return False

        """
        # approach 2: O(m * n^2)

        seen = set()

        for word in words: # O(n)
            for i in range(len(word)): # O(k)
                framed_word = word[:i] + '*' + word[i+1:] # O(k)

                if framed_word in seen:
                    return True
                else:
                    seen.add(framed_word)

        return False
        """

        """
        # approach 3: O(m * n^2)

        words_set = set(words)

        for word in words: # O(n)
            for i in range(len(word)): # O(k)
                for ascii_i in range(97, 123): # O(1)
                    ch = chr(ascii_i)

                    if ch == word[i]: continue

                    framed_word = word[:i] + ch + word[i+1:] # O(k)

                    if framed_word in words_set:
                        return True

        return False
        """