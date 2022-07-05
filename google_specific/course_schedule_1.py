"""
For optimized code refer course_schedule_1_2
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.in_d = 0
        self.neighbors = []


class Solution:
    def canFinish(self, num_courses: int, prerequisites) -> bool:
        graph_nodes_map = {}

        for i in range(0, num_courses):
            graph_nodes_map[i] = Node(i)

        for prereq in prerequisites:
            parent = prereq[1]
            child = prereq[0]
            graph_nodes_map[parent].neighbors.append(graph_nodes_map[child])
            graph_nodes_map[child].in_d += 1

        all_parent_nodes = [node for _, node in graph_nodes_map.items() if node.in_d == 0]
        visited = set()
        recursion_stack = set()
        cycle_in_graph = False

        def dfs(node):
            nonlocal cycle_in_graph

            recursion_stack.add(node)

            for neighbor in node.neighbors:
                if neighbor in recursion_stack:
                    cycle_in_graph = True
                    return False

                if neighbor in visited:
                    continue

                visited.add(neighbor)
                dfs(neighbor)

            recursion_stack.remove(node)

        for parent_node in all_parent_nodes:
            visited.add(parent_node)
            dfs(parent_node)

        if len(visited) < num_courses or cycle_in_graph:
            return False

        else:
            return True
