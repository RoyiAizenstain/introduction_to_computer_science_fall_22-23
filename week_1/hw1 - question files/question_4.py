# ************************ HOMEWORK 1 QUESTION 4 **************************
def question_4(input_list):
    ### WRITE CODE HERE
    number_of_elaborate_numbers = 0
    sum_of_elaborate_numbers = 0
    for number in input_list:
        if number == 0:
            break
        if number == 1:
            continue
        sum_of_dividers_of_number = 1
        i = int(number / 2)
        while i != 1:
            if number % i == 0:
                sum_of_dividers_of_number += i
            i = i - 1
        if sum_of_dividers_of_number == number:
            number_of_elaborate_numbers += 1
            sum_of_elaborate_numbers += number

    if number_of_elaborate_numbers != 0:
        print(round(sum_of_elaborate_numbers / number_of_elaborate_numbers, 2))
    else:
        print(0)

