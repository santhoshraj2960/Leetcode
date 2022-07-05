# NOTE: this is different form course_schedule_1 but the idea is same as course_schedule_1
from collections import defaultdict, deque


class Solution:
    def findOrder(self, num_courses: int, prerequisites):
        num_of_prereq_to_course_map = defaultdict(int)
        course_prereq_map = defaultdict(list)
        topological_order_or_completed_courses = []

        for p in prerequisites:
            course_prereq_map[p[1]].append(p[0])
            num_of_prereq_to_course_map[p[0]] += 1

        zero_prereq_courses = deque(
            [course for course in range(num_courses) if course not in num_of_prereq_to_course_map])

        while zero_prereq_courses:
            curr_course = zero_prereq_courses.popleft()
            for depedent_course in course_prereq_map[curr_course]:
                num_of_prereq_to_course_map[depedent_course] -= 1
                if num_of_prereq_to_course_map[depedent_course] == 0: zero_prereq_courses.append(depedent_course)

            topological_order_or_completed_courses.append(curr_course)

        return topological_order_or_completed_courses if len(
            topological_order_or_completed_courses) == num_courses else None


"""
Time: O(V + E) V is the number of vertices (or courses) and E is the number of edges (or len of prereq) in the imaginary graph

Space: O(V + E)
"""