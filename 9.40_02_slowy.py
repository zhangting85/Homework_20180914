
from random import randint

#只写了生成10搜船的过程。其他类似9.40_01偷懒没写了。

#各种类型船的分数 就按照index来排了。前36个事4X3类型，中间12是2X2类型。剩下的是1X1类型。

#生成10*10的地图
board_in = []

for i in range(10):
    board_in.append(['O'] * 10)

for row in board_in:
    print(" ".join(row))

ship=[]


def ship3(board_in):
    list=[]
    row=randint(0,len(board_in)-4)
    col=randint(0,len(board_in)-3)
    if([row,col] not in list):
        for i in range(4):
            for j in range(3):
                list.append([row+i,col+j])
    return list

count=0
while (count < 3):
    flag = 0
    ship3list = ship3(board_in)
    for item in ship3list:
        if item in ship:
            flag = 1
            break

    if (flag == 0):
        for item in ship3list:
           ship.append(item)

        count = count + 1


print(ship)



def ship2(board_in):
    list=[]
    row=randint(0,len(board_in)-2)
    col=randint(0,len(board_in)-2)
    if([row,col] not in list):
        for i in range(2):
            for j in range(2):
                list.append([row+i,col+j])
    return list


count=0
while (count < 3):
    flag = 0
    ship2list = ship2(board_in)
    for item in ship2list:
        if item in ship:
            flag = 1
            break

    if (flag == 0):
        for item in ship2list:
            ship.append(item)

        count = count + 1


def ship1(board_in):
    row = randint(0, len(board_in) - 2)
    col = randint(0, len(board_in) - 2)
    return [row,col]

count=0
while (count < 3):
    m=ship1(board_in)
    if(m not in ship):
        ship.append(m)
        count=count+1


print(len(ship))
print(ship)









