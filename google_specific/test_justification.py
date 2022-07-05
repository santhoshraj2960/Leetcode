from collections import deque


def distribute_words_in_line(words_list, max_width):
    if len(words_list) == 1:
        return words_list
    num_of_words = len(words_list)  # 3
    num_of_blanks = num_of_words - 1  # 2

    sum_of_len_of_words = sum(len(s) for s in words_list)  # 13

    width_remaining_after_fitting_words = (max_width - sum_of_len_of_words)  # 3
    num_of_spaces_for_each_blank = width_remaining_after_fitting_words // num_of_blanks  # 1
    num_of_additional_spaces = width_remaining_after_fitting_words % num_of_blanks  # 1

    justified_line = []
    for word in words_list:
        justified_line.append(word)
        justified_line.append(' ' * num_of_spaces_for_each_blank)

        if num_of_additional_spaces:
            justified_line.append(' ')
            num_of_additional_spaces -= 1

    return justified_line[:-1]


def justify_words(words_list, max_width):
    justified_lines = []
    words_list = deque(words_list)
    len_of_single_blank = 1

    while words_list:
        line = []
        len_of_line = 0

        while len_of_line < max_width and words_list:
            if len(words_list[0]) + len_of_line <= max_width:
                word = words_list.popleft()
                line.append(word)
                len_of_line += (len(word) + len_of_single_blank)
            else:
                break

        justified_lines.append(distribute_words_in_line(line, max_width))

    return justified_lines


print(justify_words(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(justify_words(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
print(justify_words(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
     "is", "everything", "else", "we", "do"], 20))
"""
print(distribute_words_in_line(["This", "is", "an"], 16))
print(distribute_words_in_line(["example", "of", "text"], 16))
print(distribute_words_in_line(["justification."], 16))
print(distribute_words_in_line(["Science", "is", "what", "we"], 20))
"""

"""
justified_lines [['This', '    ', 'is', '    ', 'an'], 
['example', ' ', ' ', 'of', ' ', 'text'],
["justification."]]
words_list = ["justification."]
line = ["justification."]
len_of_line = 15
max_width = 16
"""