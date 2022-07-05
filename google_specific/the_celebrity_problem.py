"""
- Notice how the
    - comments you have added adds ease of understanding in the code
    - variable names "prosp_celeb", "common_people" adds ease of understaning
"""
from collections import defaultdict


# O(n) time and O(1) space
def get_if_celebrity_in_party(mat):
    num_of_people_at_party = len(mat)

    for prosp_celeb in range(num_of_people_at_party):

        num_of_people_who_knows_prosp_celeb = 0

        for common_people in range(num_of_people_at_party):

            if mat[common_people][prosp_celeb] == 1:
                num_of_people_who_knows_prosp_celeb += 1

        if num_of_people_who_knows_prosp_celeb < num_of_people_at_party - 1:
            # This person is not a celebrity
            continue

        # This person could be a celeb. But we need to ensure this person knows NO OTHER person at party
        num_of_people_prosp_celeb_knows = 0

        for general_people in range(num_of_people_at_party):

            if mat[prosp_celeb][general_people] == 1:
                num_of_people_prosp_celeb_knows += 1
                break

        if num_of_people_prosp_celeb_knows == 0:
            return prosp_celeb

    return -1


# O(n) time and O(n) space
def get_celebrity_in_party(mat):
    num_of_people_at_party = len(mat)
    num_of_people_who_knows_person_i_dict = defaultdict(int)
    possible_celebs_list = []

    for i in range(len(mat)):

        num_of_people_i_knows = 0

        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                num_of_people_who_knows_person_i_dict[j] += 1
                num_of_people_i_knows += 1

        if num_of_people_i_knows == 0:
            possible_celebs_list.append(i)

    for person in possible_celebs_list:
        # ******* NOTE '-1' in the following line *****
        if num_of_people_who_knows_person_i_dict[person] == num_of_people_at_party - 1:
            return person

    return -1


m = [[0, 1, 0],
     [0, 0, 0],
     [0, 1, 0]]
print(get_if_celebrity_in_party(m))

