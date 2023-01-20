print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

room1 = input("You are in a room with two doors. Which one are you choosing? Type 'left' or 'right'. ")



if room1 == "left":
    room2 = input("You\'ve come to a lake. You see an island in the lake. Wait for swim or wait for the boat? Type 'swim' or 'wait'. ")
    if room2 == "wait":
        room3 = input("In the island you see an abandoned cottage. Inside there are three doors with differen colors. Which one are you choosing? Type 'red', 'yellow' or 'blue'. ")
        if room3 == "yellow":
            print("You found the treasure!!")
        elif room3 == "red":
            print("Burned by fire. Game Over.")
        elif room3 == "blue":
            print("Eaten by bests. Game Over.")
        else:
            print("Game Over.")
    elif room2 == "swim":
        print("Attacked by sharks. Game Over.")
    else:
        print("Game Over.")
elif room1 == "right":
    print("Fell into a hole. Game Over.")
else:
    print("Game Over")
