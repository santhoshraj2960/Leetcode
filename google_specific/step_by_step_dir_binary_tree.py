from lowest_common_ancestor import get_lca_main
"""

Func doc string
Can I assume that source and dest val will be present in the tree?
Can both the source and dest values be same?

"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right=right

# approach 1 (See how we used a single function find_path_from_node_to_lca to replace 2 funs in approach 2)
def get_dirs(root, source_val, dest_val):

    def find_path_from_node_to_lca(node, target_val):
        nonlocal path_from_parent_to_child, target_val

        if not node:
            return False

        if node.val == target_val:
            path_from_parent_to_child = list(recursion_stack)
            return

        recursion_stack.append('L')
        find_path_from_node_to_lca(node.left, target_val)
        recursion_stack.pop()

        recursion_stack.append('R')
        find_path_from_node_to_lca(node.right, target_val)
        recursion_stack.pop()

    lca = None
    find_lca(root)

    recursion_stack = []
    path_from_parent_to_child = []
    find_path_from_node_to_lca(lca, source_val)
    source_to_lca = ['U'] * len(path_from_parent_to_child)

    path_from_parent_to_child = []
    find_path_from_node_to_lca(lca, dest_val)

    return ''.join(source_to_lca + path_from_parent_to_child)



# approach 2
def get_dirs(root, source_val, dest_val):
    lca_node = get_lca_main(root, source_val, dest_val)

    source_to_lca_path_str = ''
    path = []

    def get_path_from_source_to_lca(node):
        nonlocal source_to_lca_path_str
        if not node:
            return

        if node.val == source_val:
            source_to_lca_path_str = ''.join(path)
            return

        else:
            path.append('U')
            get_path_from_source_to_lca(node.left)
            get_path_from_source_to_lca(node.right)
            path.pop()


    get_path_from_source_to_lca(lca_node)

    lca_to_dest_path_str = ''
    path = []

    def get_path_from_lca_to_dest(node):
        nonlocal lca_to_dest_path_str

        if not node:
            return

        if node.val == dest_val:
            lca_to_dest_path_str = ''.join(path)
            return

        else:
            path.append('L')
            get_path_from_lca_to_dest(node.left)
            path.pop()
            path.append('R')
            get_path_from_lca_to_dest(node.right)
            path.pop()

    get_path_from_lca_to_dest(lca_node)

    return source_to_lca_path_str + lca_to_dest_path_str

# ------------- Testcase 1 --------------
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
