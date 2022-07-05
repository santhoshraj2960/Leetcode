"""
4:18 pm
start = 0 || speed = 1
-ve positions valid
'A'
    - pos += speed
    - speed *= 2
'R'
    - if speed > 0: speed = -1
    - else speed = 1
    - No change in position
target >= 1 (+ve)

Bfs - find the shortest path
2 variables determine my state at any given time 't' => speed and position
let n represent target. At any time 't'
- I'll be in the range of "0 to 2n" in the number line. We can round it to 'n'
- I'll be at a speed of -n to +n because if I travel at a speed lesser or greater than this speed I'll go away from the target. We can round this to 'n'
- Overall time compl n ^ 2 || space compl. will be n^ 2 as well because our visited dictionary will have atmost n ^ 2 keys

target = 3
q = [ ((0,-1), 1), ((4,3), 2), ((1,-1), 2)  ]
visited = {
(0, 1), (1, 2), (0,-1), (4,3), (1,-1)
}
pos = 1
speed = 2
steps = 1

op_1
new_speed =  4 || new_pos = 3

op_2
new_speed = -1 || new_pos = 1
"""
"""
target = 5
0 -> 1 -> 3 -> 7 ->
0 A-> 1 A-> 3 A-> 7 R-> 7 A-> 6 A-> 4 R->
0 A-> 1 A-> 3 R-> 3 A-> 2 
"""
from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        visited = set()
        state = (0, 1)  # pos, speed
        steps = 0
        q.append((state, steps))
        visited.add(state)

        while q:
            (pos, speed), steps = q.popleft()

            if pos == target:
                return steps

            # option 1 'A'
            new_speed = speed * 2
            new_pos = pos + speed
            if (new_pos, new_speed) not in visited:
                # if new_pos is greater than (or equal to) twice the size of target, then don't queue it
                # -10, -9, -8,...-1,0,1,...8, 9, 10
                # if the target is 5,
                #   the distance you have to travel is 0 to 5 (distance 5)
                #   but if you reach 11 at some time 't', now you have to travel from 11 to 5 (distance 6)
                #   Therefore it doesn't make sense to jump to anypoint greater than 10 at any given time 't', because
                #   the car has to travel more distance (from any point greater than 10) to reach target, compared to
                #   reaching 10 from the initial position (which is 0)
                if abs(target - new_pos) < target:  # same as -> if abs(new_pos) < target * 2:"
                    q.append(((new_pos, new_speed), steps + 1))
                    visited.add((new_pos, new_speed))

            # option 2 'R'
            new_speed = -1 if speed > 0 else 1
            new_pos = pos
            if (new_pos, new_speed) not in visited:
                if abs(target - new_pos) < target:  # same as -> if abs(new_pos) < target * 2:
                    q.append(((new_pos, new_speed), steps + 1))
                    visited.add((new_pos, new_speed))


s = Solution()
"""print(s.racecar(6))
print(s.racecar(100))
print(s.racecar(1000))
print(s.racecar(9999))
print(s.racecar(10000))"""

print(s.racecar(10000))