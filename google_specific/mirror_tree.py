# https://practice.geeksforgeeks.org/problems/mirror-tree/1/

# time O(n)
# space O(h)

def mirror(self, root):
    node = root
    if not node:
        return None

    temp_left_node = node.left # *********** IMPTNT ***************
    node.left = self.mirror(node.right)
    node.right = self.mirror(temp_left_node) # ********* temp_left_node ***********

    return node