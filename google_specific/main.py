
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
"""
Change font style to Consolas in google doc. CLOSE pycharm, slack, outlook, intellij

UNDERSTAND THE QUESTION FULLY (ASK CLARIFYING QUESTIONS IF NEEDED) BEFORE STARTING TO CODE. EG: REMEMBER PAYPAL SLIDING
WINDOW MAX https://leetcode.com/problems/sliding-window-maximum/
Another eg: see function check_if_word_1_pred_word_2_WRONG in longest_string_chain problem.
Use the following statement for assumptions "Is it safe to assume my input will ...."
After digesting the question fully, tell the interviewer "Let me think about the different solutions that come to my mind
for a few seconds. And then we can brainstroam the solution and then see if we can improvise further. (THINK OUT LOUD). 

Think out loud -> Interviewer should understand what approach you plan to take -> After explaining your approach ->
write down a pseudocode if possible -> Do a dry run with a sample input using pseudocode if possible (refer 
https://leetcode.com/submissions/detail/709097086/ and https://leetcode.com/submissions/detail/709049258/) and then ->
Ask him "What do you think about my approach? 
 Is this a good place to start?"

Behaviour questions -> Try to use the STAR approach by Rahul https://youtu.be/DpSz17Cf-ZE?t=563

Come up with a naive or easy solution first. Explain it to interviewer and ask them if they are happy with that.
If you try to come up with the most efficient solution first. Sometimes the interviewer might not even expect you. You
are burdening yourself and decreasing your prob of success in the interview.
eg: spiral matrix -> fb interview -> you decided to not use O(n) space and hence complicated the code
eg: minimum_platforms problem. If
interviewer is happy with n log n solution, the probability of you getting it correct is higher then the prob of getting
the O(n) solution

Once the interviewer is happy with the approach -> Try running a few testcases with the idea you discussed with the 
interviewer inside a comments (""" """)  block -> explain your time and space complexities even before the interviewer 
asks you. 

After you write the code (or after pseudocode), verbally run your solution through a couple of test cases
Refer student_attendance_record_2 for walking through solutions involving RECURSION  

Before beginning to code, try to come up with a broad range of inputs (3 to 5 variants) to make sure you can handle
corner cases before interviewer points out.. Remember what happened in fb intern interview spiral matrix??
eg: handling -ve numbers in multiply 2 strings

Try to think of diff tools you can leverage to solve problems
    - Linkedlists (DLL in LRU Cache)
    - Deque (Circular tour)

In an array of integers (having both + and - numbers). eg: [2, 0 , 1, -2, -3, 4, ..], if the sum of numbers from i'th
position (assume index 0 => element 2) to j'th position (assume index 4 => element -3) is -ve, no matter where you
start (in between i and j), the continuous subarray ending at index j will be negative.

See how you categorized the different cases lowest_common_ancestor get_lca_main func


Try to include docstring in any helper functions you write (Add docstrings ONLY after coming up with a working code)
https://pandas.pydata.org/docs/development/contributing_docstring.html
Refer multiply_two_strings.py

Learn where SortedDict will be useful (eg: stock_price_fluctuations)

Questions to ask interviewer
- What is the one best thing about working at ...?
- What is the work you and your team do at ...?
- What motivated to choose the company or the team?

Thanks for your time today Phantasmagoric Covariate:). It was nice talking to you. As i mentioned, you did pretty well, only few stuff to focus on. Here is a list of the points 
i mentioned so you can use them for any interview
- Ask as many clarification questions as you can. Make sure you understood the problem 100% before you start. Also, try to understand all the edge cases in the input. (questions like is 
this going to be an integer, is it going to be valid domain, Is it going to fit in memory are very good questions to ask) . You are asking good questions, please keep it up.
- Summarise your solution as comment. This is good for you and the interviewer. and give an example to describe your algorithm. your description was good but as I mentioned, try to be more concise.
- Discuss the time and space complexity always before you start the implementation. Write it down as well.
- Always try to write clean code. This includes using helper functions, good variables names, and never copy/paste code. 
- Always choose the correct return type.
- Remember not to do the calculation and the formatting in the same function.
- When you finish the implementation, you need to write as many meaningful test cases as you can, especially the edge cases. Do not just use the example provided.

good luck with your coming Google interview
Cheers

"""
class Solution:
    def minJumps(self, arr, n):
        '''

        arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

        ind = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        jmp = [1, 4, 7, 10, 10, 7, 10, 10, 10, 10, 10]

        jump_to[1, 10, 10]
        '''
        if n == 1:
            return 0

        memo = [-1] * len(arr)
        '''
        res_arr = [float('inf')] * len(arr)
        res_arr[-1] = 0
        j = len(arr)
        for i in range(len(arr) - 1, -1, -1):
            while j > i:
                if res_arr[i] = min(res_arr[j] + 1, res_arr[i])
                j -= 1  
        '''
        def min_jumps(ind):
            max_jump_to_ind = ind + arr[ind]

            if max_jump_to_ind >= len(arr) - 1:
                return 1

            if arr[ind] == 0:
                return float('+inf')

            if memo[ind] != -1:
                return memo[ind]

            current_min_num_jumps = float('+inf')

            for j in range(ind + 1, max_jump_to_ind + 1):
                current_min_num_jumps = min(current_min_num_jumps, min_jumps(j))

            if current_min_num_jumps == float('+inf'):
                return float('+inf')

            memo[ind] = 1 + current_min_num_jumps

            return memo[ind]

        min_jumps_res = min_jumps(0)

        if min_jumps_res == float('+inf'):
            return -1
        else:
            return min_jumps_res


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hello')
    print_hi('PyCharm')
    s = Solution()
        arr = [
    n = len(arr)
    print(s.minJumps(arr, n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
