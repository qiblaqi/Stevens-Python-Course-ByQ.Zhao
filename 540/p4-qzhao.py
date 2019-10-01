"""
This is a program intend to tell user to guess a number 
and answer the user if they get the right answer or not.


Written by Qi Zhao
"""

import random as rd

def get_usr_number(Msg):
    #make sure to get the valid number 
    temp = input(Msg)
    try:
        number = int(temp)
    except ValueError:
        print(f"'{temp}' is not a number,please input a number! ")
        number = get_usr_number(Msg)
    return number

def take_a_guess(target,usr_guess):
    #examine usr each input is matched and give user feedback
    if usr_guess > target:
        return 1
    elif usr_guess == target:
        return 0
    else:       
        return -1

def give_feedback(game_result,attempts,usr_name):
    #determine the game feedback based on the take_a_guess function 
    if game_result == 0:
        print(f"Good job, {usr_name}! You guessed my number in {attempts} guesses!")
    elif game_result == 1:
        print("Your target is too high.")
    elif game_result == -1:
        print("Your target is too low.")

def main():
    #get the target and then give usr feedback
    target = rd.randint(1,20)
    game_result = 0
    usr_name = input("Hello! What is your name? ")
    for i in range(6):
        print(f"Attemps {i+1}: ")
        usr_guess = get_usr_number("Take a guess. ")
        game_result = take_a_guess(target,usr_guess)
        give_feedback(game_result,i+1,usr_name)
        if game_result == 0:
            break
    if game_result != 0:
        print(f"The number I was thinking of was {target}")

if __name__ == '__main__':
    main()
