
#双人游戏：input的时候改成了两次就可以吗？
from random import randint

board_in = []

for i in range(5):
    board_in.append(['O'] * 10)

for row in board_in:
    print(" ".join(row))



def randow_row(board_in):
    return randint(0, len(board_in) - 1)


def randow_col(board_in):
    return randint(0, len(board_in[0]) - 1)

ship=[]
number=0
while(number<5):
    x=randow_row(board_in)
    y=randow_col(board_in)
    if([x,y] not in ship):
        ship.append([x,y])
        number=number+1

print(ship)

count=0
for i in range(3):
    count=count+1
    print("Turn",count)

    print("第一个人请输入：")
    guess_row = int(input("猜一下船在第几行："))
    guess_col = int(input("猜一下船在第几列："))

    print("第二个人请输入：")
    guess_row2 = int(input("猜一下船在第几行："))
    guess_col2 = int(input("猜一下船在第几列："))

    if(board_in[guess_row][guess_col]=="X" or board_in[guess_row2][guess_col2] == "X" ):
        print("你们已经猜过这个位置了！")

    board_in[guess_row][guess_col] = "X"
    board_in[guess_row2][guess_col2]="X"

    if ([guess_row, guess_col] in ship or [guess_row2,guess_col2] in ship):
        print("恭喜你猜对了！")
        break
    elif guess_row not in range(len(board_in)) or guess_col not in range(len(board_in[0])) or guess_row2 not in range(len(board_in) or guess_col2 not in range(len(board_in[0]))):
        print("超出范围了！")

    else:
        print("你没有击中我的船！")
    if (count == 3):
        print("Game OVer!")












