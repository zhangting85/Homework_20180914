
from random import randint

board_in = []

for i in range(5):
    board_in.append(['O'] * 5)

for row in board_in:
    print(" ".join(row))


for turn in range(4):
    print("Turn",turn+1)

    def randow_row(board_in):
        return randint(0, len(board_in) - 1)


    def randow_col(board_in):
        return randint(0, len(board_in) - 1)


    ship_row = randow_row(board_in)
    ship_col = randow_col(board_in)

    print(ship_row)
    print(ship_col)

    guess_row = int(input("猜一下船在第几行："))
    guess_col = int(input("猜一下船在第几列："))



    if (guess_row == ship_row and guess_col == ship_col):
        print("恭喜你猜对了！")
        break
    else:
        if guess_row not in range(len(board_in)) or guess_col not in range(len(board_in)):
            print("超出了范围！")
        elif (board_in[guess_row][guess_col] == "X"):
            print("这个位置已经猜过了！")
        else:
            print("你没有击中我的船！")
    if(turn==3):
        print("Game OVer")
    if(guess_row in range(len(board_in)) and guess_col in range(len(board_in))):
        board_in[guess_row][guess_col]="X"


