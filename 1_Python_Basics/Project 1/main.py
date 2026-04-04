#Project 1 : Snake, Water Gun
'''
1 for snake,
-1 for water
0 for gun
'''
import random

print("---- SNAKE, WATER AND GUN ----")
computer_choice = random.choice([-1, 0, 1])
your_choice = input("Enter your choice (s/w/g): ")

youDict = {"s": 1, "w": -1, "g": 0}
compDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[your_choice]
computer = computer_choice

print(f"Your choice: {compDict[you]} \nComputer's choice: {compDict[computer]}")

if ( computer == you ):
    print("Its a draw")
    
else: 

    if ( computer == -1 and you == 1 ):
        print("You Won")
    elif ( computer == -1 and you == 0 ):
        print("You Lose")

    elif ( computer == 1 and you == -1 ):
        print("You Lose")
    elif ( computer == 1 and you == 0 ):
        print("You Won")
    
    elif( computer == 0 and you == 1 ):
        print("You Lose")
    elif( computer == 0 and you == -1):
        print("You Won")
    
    else:
        print("Something went wrong")

