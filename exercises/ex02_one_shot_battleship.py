"""EX02 - One Shot Battleship!"""

__author__ = "730665579"

grid: int = 4
secret_row: int = 3
secret_column: int = 2
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C" #setting values

result_box: str = " "
rowchoice: int = int(input('Guess a row: '))
while rowchoice > grid or rowchoice <= 0: 
    rowchoice = int(input(f"The grid is only {grid} by {grid}. Try again: ")) #evaluate if correct row size

colchoice: int = int(input('Guess a column: '))
while colchoice > grid or colchoice <= 0: 
    colchoice = int(input(f"The grid is only {grid} by {grid}. Try again: ")) #eval corrct col size

if rowchoice == secret_row and colchoice == secret_column:
    result_box = RED_BOX
else: 
    result_box = WHITE_BOX #eval if hit or miss
    
row_counter = 1
while row_counter <= grid: 
    row_string: str = " "
    column_counter: int = 1  #set vals
    while column_counter <= grid: 
        if column_counter == colchoice and row_counter == rowchoice: 
            row_string += result_box
            column_counter += 1
        else: 
            row_string += BLUE_BOX 
            column_counter += 1  #loop though setting blue red and white boxes
    row_counter += 1
    print(row_string)  #line by line printing

if rowchoice == secret_row and colchoice == secret_column:
    print('Hit!')
    result_box = RED_BOX
else: 
    print('Miss!')
    result_box = WHITE_BOX #eval if hit or miss


if result_box == WHITE_BOX: 
    if colchoice == secret_column: 
        print('Close! Correct column, wrong row.')
    elif rowchoice == secret_row: 
        print('Close! Correct row, wrong column.') #gives clue if close