# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        max_sum = float('-inf')

        def helper(node):
            nonlocal max_sum

            if not node:
                return 0

            left_subtree_sum = helper(node.left)
            right_subtree_sum = helper(node.right)
            curr_node_val = node.val

            max_sum_at_node = max(curr_node_val, curr_node_val + left_subtree_sum, curr_node_val +
                                  right_subtree_sum, curr_node_val + right_subtree_sum + left_subtree_sum)

            max_sum = max(max_sum, max_sum_at_node)

            # NOTE: You cannot return max_sum_at_node coz when you choose a particular node and it's parent,
            # you can either choose it's left branch or it's right branch. You cannot choose both
            # parent_of_node -> node -> (left_branch or right branch)
            # eg test_case [5,4,8,11,null,13,4,7,2,null,null,null,1] => Draw the tree and see node 8
            return_val = max(curr_node_val, curr_node_val + left_subtree_sum,
                             curr_node_val + right_subtree_sum)

            return return_val

        helper(root)

        return max_sum