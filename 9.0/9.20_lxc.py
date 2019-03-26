from random import randint
from time import sleep

def print_board():
    model = input("请选择难度：（1.简单 2.困难）")
    if model.isdigit() == True:
        if int(model) == 1:
            str = "---".join(["O"]*5)
            for row in range(5):
                print(str)
        elif int(model) == 2:
            str = "---".join(["O"] * 10)
            for row in range(10):
                print(str)
        else:
            print("请输入1或2")
            print_board()
        return int(model)
    else:
        print_board()

def random_row_col(model):
    if model == 1:
        ship_row = randint(1,5)
        ship_col = randint(1,5)
        return ship_row, ship_col

    elif model == 2:
        ship_row = randint(1, 10)
        ship_col = randint(1, 10)

        return ship_row, ship_col

def guess(random_row_col):
    print(random_row_col)
    on_off = 0
    j = 0
    while on_off == 0:
        num = 4
        for i in range(num):
            guess_row = input("猜一下船在第几行")
            guess_col = input("猜一下船在第几列")
            if guess_row.isdigit() == True and guess_col.isdigit() == True:
                if int(guess_row) == random_row_col[0] and int(guess_col) == random_row_col[1]:
                    print("恭喜你，猜对了！")
                    again = (input("1.在玩一次 2.不了"))
                    if  int(again) == 1 :
                        break
                    else:
                        on_off = 1
                        pass

                elif int(guess_row) != random_row_col[0] or int(guess_col) != random_row_col[1]:
                    num -= 1
                    if num > 0:
                        print("你没有击中我的船，你还有{}次机会".format(num))
                    elif num == 0:
                        if input("再玩一次？(y/n)").lower() == "y":
                            pass
                    elif num == 0 :
                        if input("再玩一次？(y/n)").lower() == "n":
                            on_off = 1
            else:
                num -= 1
                if num > 0:
                    print("请输入数字，你还有{}次机会".format(num))
                if num == 0:
                    if input("再玩一次？(y/n)").lower() == "n":
                        print("游戏结束")
                        on_off = 1
if __name__ == "__main__":
    model =print_board()
    random_row_col = random_row_col(model)
    guess(random_row_col)
