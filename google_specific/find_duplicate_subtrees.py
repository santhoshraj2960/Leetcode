# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [N,4,N,2,N,
# 1,
# N,4,N,2,N,3,N,4,N]
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        visited_set = set()
        dup_subtree = {}

        def inorder(node):
            if not node:
                return 'n'

            left_ret = inorder(node.left)
            right_ret = inorder(node.right)
            tup = tuple([left_ret, node.val, right_ret])

            if tup in visited_set:
                dup_subtree[tup] = node

            visited_set.add(tup)

            return tup

        inorder(root)
        return dup_subtree.values()