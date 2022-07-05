'''
What should I return when the input array is empty?
Will my input have only open and close brackets or should I expect other alpha numeric characters also?
Is my input an array or a string?
It it is a string, should I trim off any additional blans spaces at the ends?
'''


def parenthesis_checker(x):
    arr = [ele for ele in x.strip()]
    stack = []
    brackets_dict = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    for ele in arr:
        if ele not in ['{', '}', '[', ']', '(', ')']:
            continue

        if ele in ['[', '{', '(']:
            stack.append(ele)
        else:
            if not stack:  # eg: '}'
                return False

            popped_ele = stack.pop()

            if brackets_dict[popped_ele] != ele:
                return False

    if stack:  # eg: '['
        return False

    return True

print(parenthesis_checker('}'))