"""
num_of_prereq_for_course_dict = {
1: 1
}

prerequ_to_course_dict = {
0: [1]
}

zero_indegree_courses = [0]
"""
from collections import defaultdict, deque


class Solution:
    def canFinish(self, num_courses: int, prerequisites) -> bool:
        num_of_prereq_for_course_dict = defaultdict(int)
        prerequ_to_course_dict = defaultdict(list)
        num_of_completed_courses = 0

        for prereq in prerequisites:
            num_of_prereq_for_course_dict[prereq[0]] += 1
            prerequ_to_course_dict[prereq[1]].append(prereq[0])

        zero_indegree_courses = deque([course for course in range(num_courses) if course not in num_of_prereq_for_course_dict])

        while zero_indegree_courses:
            zero_indegree_course = zero_indegree_courses.popleft()

            for dependent_course in prerequ_to_course_dict[zero_indegree_course]:
                num_of_prereq_for_course_dict[dependent_course] -= 1

                if num_of_prereq_for_course_dict[dependent_course] == 0: zero_indegree_courses.append(dependent_course)

            num_of_completed_courses += 1

        return num_of_completed_courses == num_courses

"""
time: We visit each edge exactly once in the imaginary graph constructed above. Each edge is represened by input varibale "prerequisites". 
To populate 'zero_indegree_courses', we visit all vertices ('num_courses')
O(V + E) => E represents the len of prerequisites, V represents the num_courses

space: O(V + E) 
"""