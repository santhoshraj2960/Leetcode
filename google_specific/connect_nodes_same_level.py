class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
        self.next = None


class ConnectNodesAtSameLevel:
    def __init__(self):
        self.node_height_mapping = {}

    def connect_nodes_at_same_level(self, root):
        self.construct_node_height_mapping(root, 0)
        return root

    def construct_node_height_mapping(self, node, height):
        if not node:
            return

        if height in self.node_height_mapping:
            self.node_height_mapping[height].next = node
            self.node_height_mapping[height] = node

        else:
            self.node_height_mapping[height] = node

        self.construct_node_height_mapping(node.left, height + 1)
        self.construct_node_height_mapping(node.right, height + 1)

"""
       10                       10 ------> NULL
      / \                       /      \
     3   5       =>             3 ------> 5 --------> NULL
    / \   \                    /  \           \
   4   1   2                  4 --> 1 -----> 2 -------> NULL


"""
node_10 = Node(10)
node_3 = Node(3)
node_5 = Node(5)
node_4 = Node(4)
node_1 = Node(1)
node_2 = Node(2)

node_10.left = node_3
node_10.right = node_5

node_3.left = node_4
node_3.right = node_1

node_5.right = node_2
connect_nodes_class = ConnectNodesAtSameLevel()
connect_nodes_class.connect_nodes_at_same_level(node_10)
