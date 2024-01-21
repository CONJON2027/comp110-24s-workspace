"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730665579"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
#box codes
input_user_1_str: str = input('Pick a secret boat location between 1 and 4: ')
user_1_choice: int = int(input_user_1_str)
#asks person what they want to input for there ship
if user_1_choice < 1:
    print("Error! " + input_user_1_str + ' too low!')
    exit()
elif user_1_choice > 4:
    print("Error! " + input_user_1_str + ' too high!')
    exit()
#checks to make sure that it is a valid number
input_user_2_str: str = input('Guess a number between 1 and 4: ')
user_2_choice: int = int(input_user_2_str)
#asks what person two wants to pick

if user_2_choice < 1:
    print("Error! " + input_user_2_str + ' too low!')
    exit()
elif user_2_choice > 4:
    print("Error! " + input_user_2_str + ' too high!')
    exit()
#checks to see if its a valid number

boxes: str = ""

if user_1_choice == user_2_choice:
    if user_2_choice == 1:
        boxes = RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX
    elif user_2_choice == 2:
        boxes = BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX
    elif user_2_choice == 3:
        boxes = BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX
    elif user_2_choice == 4:
        boxes = BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX
elif user_1_choice != user_2_choice:
    if user_2_choice == 1:
        boxes = WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX
    elif user_2_choice == 2:
        boxes = BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX
    elif user_2_choice == 3:
        boxes = BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX
    elif user_2_choice == 4:
        boxes = BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX

#diffret box combos 
if user_1_choice == user_2_choice:
    print(boxes)
    print('Correct! You hit the ship')
elif user_1_choice != user_2_choice:
    print(boxes)
    print('Incorrect! You missed the ship.') #logic to detrimine if the choices hit or missed the ship

