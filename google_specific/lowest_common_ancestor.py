# User function Template for python3
"""
- Can I assume that both the input values (for which I need to find LCA) are in the tree?
- What should I return if one (or both) of the inputs are not present in the tree?
- If what you return from a function does not matter, use '_' (underscore). '_' kind of means, it doesn't matter
"""
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

# Approach 1 (Best approach - Use this in interviews because approach 2 and 3 - you won't have time to type so much)
class Solution:
    def lowestCommonAncestor(self, root, source, dest):
        lca = None

        def find_lca(node):
            nonlocal lca

            if not node:
                return False

            ret_val_left = find_lca(node.left)
            ret_val_right = find_lca(node.right)

            curr_node_source_or_dest = (node.val == source.val) or (node.val == dest.val)

            if curr_node_source_or_dest + ret_val_left + ret_val_right == 2:
                lca = node

            return ret_val_left or ret_val_right or curr_node_source_or_dest

        find_lca(root)
        return lca


"""
Assumptions:
- Source and target in tree
- All the numbers are distinct

example 1 || p = 5 q = 1

node(3)
    - node(5) --> return True
        - node(6) --> False
            - node(None) --> return False
            - node(Node) --> retuen False

        - node(2) --> return False
            - node(7) --> return False
            - node(4) --> return False

        - ret_val_left = False
        - ret_val_right = False
        - curr_node_source_or_dest = True

    - node(1) --> return True


    - ret_val_left = True
    - ret_val_right = True
    - curr_node_source_or_dest = False
    - lca = 3

-------------------------------

example 2 || p = 5 q = 4

node(3)
    - node(5) --> return True
        - node(6) --> False
            - node(None) --> return False
            - node(Node) --> retuen False

        - node(2) --> return True
            - node(7) --> return False
            - node(4) --> return True

        - ret_val_left = False
        - ret_val_right = True
        - curr_node_source_or_dest = True
        - lca = 5

    - node(1) --> return False


    - ret_val_left = True
    - ret_val_right = False
    - curr_node_source_or_dest = False
"""



# Have a look at the approach that stores the parent node in a dict. Using that we can find lca too
# Approach 2
def get_lca_main(root, source_val, dest_val):
    lca_node = None

    def get_lca(node):
        nonlocal lca_node

        if not node:
            return False, False

        source_node_found_l, dest_node_found_l = get_lca(node.left)
        source_node_found_r, dest_node_found_r = get_lca(node.right)

        # Case 1: node_1 found in left sub tree and node_2 found in right sub tree
        if (source_node_found_l and dest_node_found_r) or (source_node_found_r and dest_node_found_l) and lca_node is None:
            lca_node = node
            return False, False

        # Case 2: node_1 found in left or right sub tree and current root is node_2
        elif (source_node_found_l or source_node_found_r) and (node.val == dest_val):
            lca_node = node
            return False, False

        # Case 3: node_2 found in left or right sub tree and current root is node_1
        elif (dest_node_found_l or dest_node_found_r) and (node.val == source_val):
            lca_node = node
            return False, False

        # case 4: current root is node_1 and node_2 is not yet discovered
        elif node.val == source_val:
            return True, False

        # case 5: current root is node_2 and node_1 is not yet discovered
        elif node.val == dest_val:
            return False, True

        else:
            return max(source_node_found_l, source_node_found_r), max(dest_node_found_l, dest_node_found_r)

    get_lca(root)

# ------------- Testcase 1 --------------
# Refer https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/ for tree dia
node_3 = TreeNode(3)
node_1 = TreeNode(1, node_3)

node_6 = TreeNode(6)
node_4 = TreeNode(4)
node_2 = TreeNode(2, node_6, node_4)

node_5 = TreeNode(5, node_1, node_2)

print(get_dirs(node_5, 3, 6))
print(get_dirs(node_5, 1, 4))
print(get_dirs(node_5, 4, 1))
print(get_dirs(node_5, 6, 1))

# ------------- Testcase 2 --------------
node_1 = TreeNode(1)
node_2 = TreeNode(2, node_1)
print(get_dirs(node_2, 2, 1))

# ------------- Testcase 2 --------------
node_1 = TreeNode(1)
node_2 = TreeNode(2, None, node_1)
print(get_dirs(node_2, 2, 1))


# ------------------------------------------------------------------------------------------------


# Approach 3
class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.
    def __init__(self):
        self.n1 = None
        self.n2 = None
        self.least_common_ancestor = None

    def find_lowest_common_ancestor_helper(self, root):
        if root == None:
            return False, False

        n1_found_on_l_branch, n2_found_on_l_branch = self.find_lowest_common_ancestor_helper(root.left)
        n1_found_on_r_branch, n2_found_on_r_branch = self.find_lowest_common_ancestor_helper(root.right)

        if max(n1_found_on_l_branch, n1_found_on_r_branch) == True and \
                max(n2_found_on_l_branch, n2_found_on_r_branch) == True and self.least_common_ancestor == None:
            self.least_common_ancestor = root
            return '_', '_'

        if root.data == self.n1:
            if max(n2_found_on_l_branch, n2_found_on_r_branch) == True \
                    and self.least_common_ancestor == None:
                self.least_common_ancestor = root
                return '_', '_'
            else:
                return True, False

        if root.data == self.n2:
            if max(n1_found_on_l_branch, n1_found_on_r_branch) == True \
                    and self.least_common_ancestor == None:
                self.least_common_ancestor = root
            return '_', '_'
        else:
            return False, True

        else:
        return max(n1_found_on_l_branch, n1_found_on_r_branch), max(n2_found_on_l_branch, n2_found_on_r_branch)


def lca(self, root, n1, n2):
    self.n1 = n1
    self.n2 = n2
    self.find_lowest_common_ancestor_helper(root)
    return self.least_common_ancestor
    # Code here
