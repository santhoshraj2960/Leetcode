# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> [int]:
        nodes_k_dist_from_target = []
        parents_dict = {}
        """
        {3: None
        5: 3
        1: 3
        0: 1
        8: 1
        }
        """

        def populate_parent_dict(node, parent):
            nonlocal parents_dict
            parents_dict[node] = parent
            if node.left: populate_parent_dict(node.left, node)
            if node.right: populate_parent_dict(node.right, node)

        def dfs(node, dist_from_target, caller):
            nonlocal nodes_k_dist_from_target

            if not node:
                return

            if dist_from_target == k:
                nodes_k_dist_from_target.append(node.val)
                return

            if node.left != caller: dfs(node.left, dist_from_target + 1, caller=node)
            if node.right != caller: dfs(node.right, dist_from_target + 1, caller=node)
            if parents_dict[node] not in [caller, None]: dfs(parents_dict[node], dist_from_target + 1, caller=node)

        populate_parent_dict(root, None)
        dfs(target, 0, target)
        return nodes_k_dist_from_target




