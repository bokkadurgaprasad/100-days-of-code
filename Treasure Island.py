print("Welcome to Treasure Island.")
print("Your mission is to find Treasure.")
ch1=input('You\'re at a crossroad, Where to go? Type "left" or "right".\n').lower()
if ch1 == "left":
    ch2=input('You\'ve come to the lake. There is an Island at the middle of lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if ch2 == "wait":
        ch3=input("You arrive at the Island unharmed.\nThere is a house with 3 doors.\nOne red, One yellow and One blue. Which Colour do you choose?\n").lower()
        if ch3 == "red":
            print("It's a room full of fire. Game Over.")
        elif ch3 == "yellow":
            print("yeahhhhh!!!\nYou found the Treasure! You Win!\n")
            print('''\n*******************************************************************************
          |                   |                  |                     |
 ________|________________.=""_;=.______________|_____________________|______
|                   |  ,-"_,=""     `"=.|                  |
|__________________|__"=._o`"-.        `"=._____________|__________________
          |                `"=.o`"=.      `"=.                     |
 ________|_____________________:=._o "=._."_.-="'"=.__________________|______
|                   |    _.--" , ; `"=._o." ,-"""-. ".   |
|__________________|_._"  ,. .` ` `` ,  `"-._"-.   ". '_|__________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 ________|___________| ;`-.o`"=._; ." ` '`."\` . "-. /______________|______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|__________________|_| ;     (#) `-.o `"=.`.--"o.-; ;___|__________________
___/______/______/___|o;.    "      `".o|o_.--"    ;o;___/______/______/___
/_____/______/______/_"=._o--.        ; | ;        ; ;/_____/______/______/
___/______/______/______/__"=._o--.   ;o|o;     ._;o;____/______/______/___
/_____/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/
___/______/______/______/______/_____"=.o|o.--""__/______/______/______/___
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
        elif ch3 == "blue":
            print("You enter a room of beats. Game Over.")
        else:
            print("YOu choose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell into the hole, Game Over.")

