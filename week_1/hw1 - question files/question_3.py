# ************************ HOMEWORK 1 QUESTION 3 **************************
def question_3(input_num):
    ### WRITE CODE HERE
    i = input_num
    while i != 0:
        output_i = str(i)
        for n in range(0, i):
            output_i += "*"
        output_i += str(i)
        print(output_i)
        i = i - 1
