# Snake Water Gun
# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.



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