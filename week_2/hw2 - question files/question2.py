# ************************ QUESTION 2.1 **************************
### WRITE CODE HERE
def split_words(game_words):
    """Takes words, return list of words """
    list_of_words = [""]
    word_place = 0
    for letter in range(len(game_words)):
        if game_words[letter] == "$":
            word_place += 1
            list_of_words.append("")
            continue
        list_of_words[word_place] += game_words[letter]
    return list_of_words


# ************************ QUESTION 2.2 **************************
### WRITE CODE HERE
def get_guess_result(secret_word, guess_letter, current_word):
    """Takes secret word and guessed letter and current word, returns updated current word """
    letter_place = 0
    for letter in secret_word:
        if letter == guess_letter:
            current_word[letter_place] = guess_letter
        letter_place += 1
    return current_word


# ************************ QUESTION 2.3 **************************
import random


def choose_secret_word(words_list):
    return random.choice(words_list)


### WRITE CODE HERE
def is_exist(my_list, string):
    """Takes list, returns true if string is existing"""
    for i in range(len(my_list)):
        if my_list[i] == string:
            return True
    return False


def board_format(board_list):
    """Takes list, returns a string format of the list"""
    board = ""
    counter = 0
    for letter in board_list:
        counter += 1
        if counter < len(board_list):
            board += letter + " "
        else:
            board += letter
    return board


def play_hangman(game_words):
    """Takes game words, returns hangman game"""
    secret_word = choose_secret_word(split_words(game_words))
    print("Welcome to Hangman Game!")
    attempts = int(input("Enter number of attempts: "))
    print("The word has " + str(len(secret_word)) + " letters." + " You have " + str(attempts) + " attempts.")
    user_guesses = []
    current_board = ["_"] * len(secret_word)
    print(board_format(current_board))
    while attempts > 0:
        guessed_letter = input("Guess a letter: ")
        if is_exist(user_guesses, guessed_letter):
            print("You already guessed that letter.")
            print(board_format(current_board))
            continue
        if is_exist(secret_word, guessed_letter):
            current_board = get_guess_result(secret_word, guessed_letter, current_board)
            if not is_exist(current_board, "_"):
                print("Congratulations! You guessed the word: " + secret_word)
                break
            print(board_format(current_board))
        else:
            attempts -= 1
            print("Wrong guess! Attempts remaining: " + str(attempts))
            if attempts == 0:
                print("Sorry, you've run out of attempts. The word was: " + secret_word)
                break
            print(board_format(current_board))
        user_guesses.append(guessed_letter)
