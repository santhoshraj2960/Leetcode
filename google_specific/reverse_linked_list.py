# https://leetcode.com/problems/reverse-linked-list/
"""
pn = None
1 -> 2 -> 3 -> 4 -> 5
n = 1
nn = 2
n.n = pn
pn = n
n = nn

pn=1
1 -> none || 2 -> 3 -> 4 -> 5
n = 2
nn = 3
n.n = pn
pn = n
n = nn

pn = 2
2 -> 1 -> none || 3 -> 4 -> 5
n = 3
"""


class Solution:
    def reverseList(self, node):
        if not node:
            return None

        prev_node = None

        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        return prev_node
