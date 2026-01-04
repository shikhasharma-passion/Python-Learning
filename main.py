# Snake, Water, Gun Game
# Snake, Water and Gun is a variation of the children's game "Rock-Paper-Scissors".
# In this game, players choose one of the following:
# snake, water, or gun
#
# Rules of the game:
# 1. Gun beats Snake
# 2. Water beats Gun
# 3. Snake beats Water
# 4. If both players choose the same option, the game is a tie
#
# This program uses functions and if-else statements
# to decide the winner. No GUI is used; input and output
# are handled through the terminal.



def snake():
    return "snake"
def water():
    return "water"
def gun():
    return "gun"

def check_win(player1, player2):
    if player1 == player2:
        return "it's a tie"
    elif (player1 == "snake" and player2 == "water") or \
         (player1 =="water" and player2 == "gun") or \
         (player1 == "gun" and player2 == "snake"):
     return "player1 is winner"
    else:
        return "player2 is winner"
    
def main():
       print("Welcome to Snake, Water and Gun Game")

       player1 = input("player1, enter your choice (snake/water/gun): ").lower()
       player2 = input("player2, enter your choice (snake/water/gun)").lower()


       result =check_win(player1, player2)
       print(result)


main()
