# https://leetcode.com/problems/find-leaves-of-binary-tree/
"""
dict = {
1: [4,5,3],
2: [2],
3: [1]
}
dfs_height(1)
    - dfs_height(2)
        - dfs_height(4)
            - dfs_height(None) --> return 0
            - dfs_height(None) --> return 0
            - node_ht = 1 + max(0,0) = 1

"""
from collections import defaultdict


def get_nodes_of_tree_leaf_to_root(root):
    """
    return a list of lists containing the nodes of a tree from leaves to root

    :param root: root of a binary tree
    :return: list[lists]: list of list objects containing the tree nodes

    """
    res_dict = defaultdict(list)
    res = []

    def helper(node):
        if not node:
            return 0

        ht_ret_from_left_branch = helper(node.left)
        ht_ret_from_right_branch = helper(node.right)

        node_ht_in_tree = max(ht_ret_from_left_branch, ht_ret_from_right_branch)

        res_dict[node_ht_in_tree].append(node.val)

        return 1 + node_ht_in_tree

    for i in range(len(res_dict.keys())):
        res.append(res_dict[i])

    helper(root)

    return res













































