"""
Read solutions tab solution to understand how the algo works (visualize the intuition)

https://leetcode.com/problems/distribute-coins-in-binary-tree/solution/

"""


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        """
        docstring
        """
        num_of_moves = 0

        def helper_distribute_coins(node):
            nonlocal num_of_moves

            if not node:
                return 0

            num_coins_excess_or_deficit_left = helper_distribute_coins(node.left)
            num_coins_excess_or_deficit_right = helper_distribute_coins(node.right)
            num_of_coins_excess_or_deficit_curr_node = node.val + num_coins_excess_or_deficit_left + num_coins_excess_or_deficit_right - 1

            num_of_moves += abs(num_of_coins_excess_or_deficit_curr_node)

            return num_of_coins_excess_or_deficit_curr_node

        helper_distribute_coins(root)

        return num_of_moves
