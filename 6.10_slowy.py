#Task1
prices={"banana":4,"apple":2,"orange":1.5,"pear":3}

stock={"banana":6,"apple":0,"orange":32,"pear":15}

def list_fruit(list1,list2):
    for key,value in list1.items():
        print(key)
        print("售价为{}".format(value))
        print("库存为{}".format(list2[key]))

list_fruit(prices,stock)

def total_money(list1,list2):
    money=0
    for key,value in list1.items():
        money=money+value*list2[key]
    print("总价为：{}".format(money))

total_money(prices,stock)




"""
def compute_bill(food,prices,stock):
    money=0
    for key1,value1 in food.items():
        for key2,value2 in prices.items():
            if(key1==key2):
                if(stock[key2]>food[key1]):
                    money=money+value2*food[key1]
                    stock[key2]=stock[key2]-food[key1]
                elif(stock[key2]<food[key1] and stock[key2]>0):
                    money=money+value2*stock[key2]
                    stock[key2]=0
    return print(money)
"""



prices={"banana":4,"apple":2,"orange":1.5,"pear":3,"aaa":8}
stock={"banana":6,"apple":0,"orange":32,"pear":15}
food={"banana":8,"orange":2,"apple":3}

def compute_bill(food,prices,stock):
    money=0
    for key,value in food.items():
        if(stock[key]>food[key]):
            money=money+prices[key]*food[key]
            stock[key]=stock[key]-food[key]
        elif(stock[key]<food[key]):
            money=money+prices[key]*stock[key]
            stock[key]=0
    return print(money)


compute_bill(food,prices,stock)

for key,value in stock.items():
    print(key)
    print(value)

