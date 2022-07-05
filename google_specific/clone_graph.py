"""
new_1
    - val: 1
    - neighbors = [new_1, new_4]

new_2
    - val:2
    - neighbors = [new_3]

new_3
    - val:3
    - neighbors = [new_4]

new_4
    - val:4
    - neighbors = [new_1]

seen[o_1] = new_1
seen[o_2] = new_2
seen[o_3] = new_3
seen[o_4] = new_4

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        seen = {}

        def dfs(node):
            new_node = Node(node.val)
            seen[node] = new_node

            for neighbor in node.neighbors:
                if neighbor in seen:
                    new_node.neighbors.append(seen[neighbor])
                    continue

                new_node.neighbors.append(dfs(neighbor))

            return new_node

        return dfs(node)