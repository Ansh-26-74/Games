#This is the 2nd Branch :)

import random

def MakeGrids(space):
    print("     |     |     ")
    print(f"  {space[0]}  |  {space[1]}  |  {space[2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {space[3]}  |  {space[4]}  |  {space[5]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {space[6]}  |  {space[7]}  |  {space[8]}  ")
    print("     |     |     ")

def PlayerMove(space, player):
    while True:
        n = int(input("Enter the number (1-9) to input 'X': "))
        n = n - 1
        if space[n] == ' ':
            space[n] = player
            break

def ComputerMove(space, computer):
    while True:
        n = random.randint(1,9)
        n = n-1
        if space[n] == ' ':
            space[n] = computer
            break

def CheckWinner(space,player):
    if((space[0] != ' ') and (space[0] == space[1]) and (space[1] == space[2])):
        print("YOU WIN!") if space[0] == player else print("YOU LOSE!")
    elif((space[3] != ' ') and (space[3] == space[4]) and (space[4] == space[5])):
        print("YOU WIN!") if space[3] == player else print("YOU LOSE!")
    elif((space[6] != ' ') and (space[6] == space[7]) and (space[7] == space[8])):
        print("YOU WIN!") if space[6] == player else print("YOU LOSE!")
    elif((space[0] != ' ') and (space[0] == space[3]) and (space[3] == space[6])):
        print("YOU WIN!") if space[0] == player else print("YOU LOSE!")
    elif((space[1] != ' ') and (space[1] == space[4]) and (space[4] == space[7])):
        print("YOU WIN!") if space[1] == player else print("YOU LOSE!")
    elif((space[2] != ' ') and (space[2] == space[5]) and (space[5] == space[8])):
        print("YOU WIN!") if space[2] == player else print("YOU LOSE!")
    elif((space[0] != ' ') and (space[0] == space[4]) and (space[4] == space[8])):
        print("YOU WIN!") if space[0] == player else print("YOU LOSE!")
    elif((space[2] != ' ') and (space[2] == space[4]) and (space[4] == space[6])):
        print("YOU WIN!") if space[2] == player else print("YOU LOSE!")
    else:
        return False
    return True
    
def CheckTie(space):
    for i, s in enumerate(space):
        if s == ' ':
            return False
    print("IT's A TIE!\n")
    return True

def main():
    space = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = 'X'
    computer = 'O'
    play = True


    MakeGrids(space)
    while(play):
        PlayerMove(space, player)
        MakeGrids(space)
        if(CheckWinner(space,player)):
            play = False
            break
        if(CheckTie(space)):
            play = False
            break

        ComputerMove(space, computer)
        MakeGrids(space)
        if(CheckWinner(space,player)):
            play = False
            break
        if(CheckTie(space)):
            play = False
            break

if __name__ == "__main__":
    main()