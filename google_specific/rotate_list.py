# https://leetcode.com/problems/rotate-list/
class Solution:
    def rotateRight(self, head, k: int):
        if not head: return

        len_linked_list = 0
        node = head
        while node:
            len_linked_list += 1
            node = node.next

        aux_list = [-1] * len_linked_list
        k = k % len_linked_list

        node = head
        index = 0
        while node:
            pos_after_k_shifts = (index + k) % len_linked_list
            aux_list[pos_after_k_shifts] = node.val
            node = node.next
            index += 1

        node = head
        index = 0
        while node:
            node.val = aux_list[index]
            node = node.next
            index += 1

        return head

