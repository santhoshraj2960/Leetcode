from collections import defaultdict

'''
Look at the solutions tab for other ways to solve this problem
'''


class Solution:
    def validTree(self, n: int, edges) -> bool:
        if n == 1 and not edges:
            return True

        if len(edges) < n - 1:
            return False

        valid_tree = True
        node_edge_map = defaultdict(list)
        visited = set()

        for edge in edges:
            node_edge_map[edge[0]].append(edge[1])
            node_edge_map[edge[1]].append(edge[0])

        def dfs(node, caller):
            nonlocal valid_tree

            for child_node in node_edge_map[node]:
                if child_node == caller:
                    continue

                if child_node in visited:
                    valid_tree = False
                    continue

                visited.add(child_node)
                dfs(child_node, node)

        start_node = 0
        visited.add(start_node)
        dfs(start_node, None)

        if len(visited) != n:
            valid_tree = False

        return valid_tree
