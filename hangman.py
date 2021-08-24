"""
File: hangman.py
Name: Ryan Lei
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The program will input a random world and show in dash. User only have 7 chances to guess the word.
    If the guess were wrong, user will lose 1 chance. If user input the same word two times in a row, lose 1 chance.
    If user input the same word, which is correct, two times in a row, get the same result.
    If user input the wrong form, this program will show 'Illegal format', and ask user to input again until the format
    is correct.
    After 7 chances were used, user loss the game.
    """
    # Store the secret word.
    secret_word = random_word()
    # Build the secret word in dash format.
    dash = dash_word(secret_word)
    # Store the chances that player can guess.
    new_turns = N_TURNS
    while True:
        # Show the word in dash.
        print('The word looks like: ' + str(dash))
        # Show the initial chances for user to guess the word.
        print('You have ' + str(new_turns) + ' guesses left.')
        # Let user input the guess.
        user_guess = input('Your guess: ')
        # Case-insensitive for the user input.
        input_ch = user_guess.upper()
        ans = ''
        for i in range(len(secret_word)):
            ch = secret_word[i]
            # If the word that player input were correct, show the alphabet of the secret word.
            if ch == input_ch:
                ans += input_ch
            # If the alphabet that player inputted before, show the alphabet that player inputted last time.
            # Discuss with TA Wilson on 2021/1/14
            elif dash[i].isalpha():
                ans += dash[i]
            # If the inputted alphabet were wrong, show the dash.
            else:
                ans += '-'
        # Store the alphabet that player inputted so far.
        dash = ans
        # If the input is not an alphabet, show 'illegal format' to the user.
        if not input_ch.isalpha():
            print('Illegal format.')
        # If the input is more than 1 alphabet, show 'illegal format' to the user.
        elif len(input_ch) > 1:
            print('Illegal format.')
        # If the input alphabet is not in the word, lose 1 chances.
        elif input_ch not in secret_word:
            print('There is no '+str(input_ch)+"'s in the word.")
            # Discuss with TA Wilson on 2021/1/14.
            new_turns -= 1
            # When no chance to guess, show the secret word and break the loop.
            if new_turns == 0:
                print('You are completely hung : (')
                print('The word was: '+str(secret_word))
                break
        # If player guess the alphabet correctly, show 'You are correct!'.
        elif input_ch in secret_word:
            print('You are correct!')
            # If player guess all the alphabet of the secret word correctly and still have chances to guess.
            if ans.isalpha():
                print('You win!!')
                print('The word was: '+str(secret_word))
                break


def dash_word(secret_word):
    """
    :param secret_word: str, random word.
    :return: str, return the random word in dash form.
    """
    ans = ''
    for i in range(len(secret_word)):
        if secret_word.isalpha():
            ans += '-'
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"





#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
