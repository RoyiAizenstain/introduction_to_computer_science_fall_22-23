def word_reconstruction(target_word: object, char_list: object) -> object:
    """

    :rtype: object
    """
    # Your Code Here
    if target_word == "":
        return True
    if 0 == len(char_list):
        return False
    first_letter = target_word[0]
    last_letter = target_word[-1]
    if first_letter == char_list[0] and last_letter == char_list[-1]:
        return word_reconstruction(target_word[1:len(target_word) - 1], char_list)
    elif first_letter == char_list[0]:
        return word_reconstruction(target_word[1:len(target_word)], char_list[0:len(char_list) - 1])
    elif last_letter == char_list[-1]:
        return word_reconstruction(target_word[0:len(target_word) - 1], char_list[1:len(char_list)])
    else:
        return word_reconstruction(target_word, char_list[1:len(char_list) - 1])



