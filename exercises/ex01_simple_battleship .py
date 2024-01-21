"""My first program for COMP110."""

__author__ = "730665579"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

input_user_1_str: str = input('Pick a secret boat location between 1 and 4: ' )
user_1_choice: int = int(input_user_1_str)

input_user_2_str: str = input('Guess a number between 1 and 4: ' )
user_2_choice: int = int(input_user_2_str)


if user_1_choice < 1:
    print("Error! " + input_user_1_str + ' too low!')
elif user_1_choice > 4:
    print("Error! " + input_user_1_str + ' too high!')

if user_2_choice < 1:
    print("Error! " + input_user_2_str + ' too low!')
elif user_2_choice > 4:
    print("Error! " + input_user_2_str + ' too high!')

if user_1_choice == user_2_choice:
    if user_2_choice == 1:
        boxes: str = RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX
    elif user_2_choice == 2:
        boxes: str = BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX
    elif user_2_choice == 3:
        boxes: str = BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX
    elif user_2_choice == 4:
        boxes: str = BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX
elif user_1_choice != user_2_choice:
    if user_2_choice == 1:
        boxes: str = WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX
    elif user_2_choice == 2:
        boxes: str = BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX
    elif user_2_choice == 3:
        boxes: str = BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX
    elif user_2_choice == 4:
        boxes: str = BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX


if user_1_choice == user_2_choice:
    print(boxes)
    print('Correct! You hit the ship')
else:
    print(boxes)
    print('Incorrect! You missed the ship.')
