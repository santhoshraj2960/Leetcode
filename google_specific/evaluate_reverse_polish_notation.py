# https://leetcode.com/problems/evaluate-reverse-polish-notation/

def return_evaluated_postfix_expression(expr):
    """

    :param expr:
    :return:
    """
    stack = []

    for i in range(len(expr)):
        if expr[i].isnumeric() or len(expr[i]) > 1:
            # '-11'.isnumeric() returns False. One way to find -ve numbers is by len. len will be always be greater than 1
            stack.append(expr[i])
        else:
            num_1 = stack.pop()
            num_2 = stack.pop()

            if expr[i] == '/': res = int(int(num_2) / int(num_1)) # ALERT: READ THE QUS properly: "TRUNCATE TO ZERO"
            else: res = eval(num_2 + expr[i] + num_1)

            stack.append(str(res))

    return stack[0]


print(return_evaluated_postfix_expression(["2", "1", "-"]))
print(return_evaluated_postfix_expression(["2","1","+","3","*"]))
print(return_evaluated_postfix_expression(["4","13","5","/","+"]))
print(return_evaluated_postfix_expression(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
