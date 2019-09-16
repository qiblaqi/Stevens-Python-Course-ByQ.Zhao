"""
this is a rock scissors paper game, which gamer inputs their
choice of three, the game will tell him win or not.

this game uses dictionary to store the game rules and use input function
to get the users input.

Written by Qi Zhao
"""
from random import choice

def getComputerChoice():
    """
    generate the computer's choice for the game using choice() function
    s:scissors, r:rock, p:paper   
    """
    return choice(['s','p','r'])

gameRules = {'rr':'Tie: we both chose rock','rs':'rock beats scissors - You win!','rp':'paper beats rock - I win!','sr':'rock beats scissors - I win!','ss':'Tie: we both chose scissors','sp':'scissors beats paper - You win!','pr':'paper beats rock - You win!','ps':'scissors beats paper - I win!','pp':'Tie: we both chose paper'}
ctrlKey = ' '    #initialize the control value

while ctrlKey != 'q' :
    ctrlKey = input("Please choose 'r', 'p', 's' or 'q' to quit: ")
    if ctrlKey == 'q':
        break
    usrInput = ctrlKey
    print(gameRules.get(usrInput + getComputerChoice()))    #combine two inputs and search the result in gameRules

print("Thanks for playing!")
