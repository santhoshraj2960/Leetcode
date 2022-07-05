"""
- Do not assume that the inputs are positive. Handle negative numbers as well

554
45
--------
   2 7 7 0
2 2 1 6
-------------
2 4 9 3 0
-------------

"""


def multiply_two_strings(s1, s2):
    # ------ Block to handle -ve numbers --------
    mult_factor_of_final_res = 1

    if s1 and s1[0] == '-':
        mult_factor_of_final_res *= -1
        s1 = s1[1:]

    if s2 and s2[0] == '-':
        mult_factor_of_final_res *= -1
        s2 = s2[1:]

    # ------ End of block to handle -ve numbers --------

    products_to_be_summed_up = []
    mult_factor = 1

    for i in range(len(s2) - 1, -1, -1):
        result_of_mul = mul_multi_digit_num_by_single_digit_num(s1, s2[i])
        result_of_mul = result_of_mul * mult_factor
        products_to_be_summed_up.append(result_of_mul)
        mult_factor *= 10

    # [2270, 22160, ….]

    final_res = sum(products_to_be_summed_up)
    return final_res * mult_factor_of_final_res


def mul_multi_digit_num_by_single_digit_num(multi_dig_num, single_dig_num):
    """
    Multiplies a sigle digit number with a multi digit number and returns the prod res

    :param self:
    :param multi_dig_num: 554
    :param single_dig_num: 1
    :return: 554
    """
    string_to_dig_dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
    sig_dig_num = string_to_dig_dict[single_dig_num]
    carry = 0
    res = 0
    mult_factor = 1

    for i in range(len(multi_dig_num) - 1, -1, -1):
        curr_dig_of_multi_dig_num = multi_dig_num[i]
        curr_dig_of_multi_dig_num = string_to_dig_dict[curr_dig_of_multi_dig_num]
        prod = sig_dig_num * curr_dig_of_multi_dig_num
        prod += carry  # 27

        remainder = prod % 10
        quotient = prod // 10
        res = (remainder * mult_factor) + res  # 70
        carry = quotient
        mult_factor *= 10

    res = carry * mult_factor + res

    return res


print(multiply_two_strings("-554", "45"))
print(multiply_two_strings("45", "554"))
print(multiply_two_strings("545", "554"))
print(545 * 554)
print(multiply_two_strings("54589", "554123"))
print(54589 * 554123)