# ************************ HOMEWORK 1 QUESTION 2 **************************
def question_2(spell, witches_num):
    ### WRITE CODE HERE
    if spell == "Alohomora!":
        if 0 == witches_num % 2:
            print("Doors Unlocked")
        else:
            print("Windows Unlocked")
    elif spell == "Lumos!":
        if 0 == witches_num % 2:
            print("Light")
        else:
            print("")
    elif spell == "Nox!":
        if 0 == witches_num % 2:
            print("Darkness")
        else:
            print("")
    elif spell == "Riddikulus!":
        if 0 == witches_num % 2:
            print("")
        else:
            print("Funny")
    else:
        print("")
