"""
NOTE: See how you break down the solution (as below)
- Naive approach takes O(n^2)
- Trying to solve with a better approach || may be "n log n"?
    -- But (n log n) involves sorting

sort_by_offense = [[1,5], [4,3], [10,4]]
sort_by_defence = [[4,3], [10,4], [1,5]]

visited = []
p1 = (10,4)
 - p2 = (1,5)

"""


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        visited = set()
        weak_players = 0
        properties = [tuple(prop) for prop in properties]
        # NOTE: reverse sort by the "defence" to handle cases [[7,6],[7,7]] => num_of_weak_players = 0
        # Look at the failed submissions to know where you went wrong
        sorted_by_offence = sorted(properties, key=lambda x: (x[0], -x[1]))
        player_with_highest_defense = sorted_by_offence[-1]

        for player in sorted_by_offence[::-1]:
            if player[1] < player_with_highest_defense[1]:
                weak_players += 1

            if player[1] > player_with_highest_defense[1]: player_with_highest_defense = player

        return weak_players

        """
        sort_by_defence = sorted(properties, key=lambda x: x[1]) # Use this as a stack

        for player_1 in sorted_by_offence[::-1]:

            while sort_by_defence and sort_by_defence[-1][1] > player_1[1]:
                player_2 = sort_by_defence.pop()

                if player_2 in visited: weak_chars += 1

            visited.add(player_1)

        return weak_chars
        """
s = Solution()
print(s.numberOfWeakCharacters([[9,7], [9,6]]))
"""print(s.numberOfWeakCharacters([[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]))
print(s.numberOfWeakCharacters([[7,7],[1,2],[8,10],[4,3],[1,5],[1,5]]))
print(s.numberOfWeakCharacters([[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]))
print(s.numberOfWeakCharacters([[1,1],[2,1],[2,2],[1,2]]))"""