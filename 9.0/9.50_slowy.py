
def is_even(x):
    """
    判断x是否是偶数
    :param x: 
    :return: 
    """
    if(type(x)!=int and type(x)!=float):
        print("您的输入不合法，请重新输入！")
    elif(x%2==0):
        print("{}是偶数".format(x))
        return True
    else:
        print("{}不是偶数".format(x))
        return False

is_even([1,2])


def is_int(x):
    """
    判断x是否是整数
    :param x: 
    :return: 
    """
    if(type(x)==int):
        print("{}是整数".format(x))
    elif(int(x)==x):
        print("{}也是整数".format(x))
    else:
        print("{}不是整数".format(x))

is_int(-1.1)

#第一种方法 求除数
def digit_sum(n):
    """
    求n各个位上的数字之和。
    :param n: 
    :return: 
    """
    length=len(str(n))
    print(length)
    sum_total=0
    for i in range(length-1,-1,-1):
        dig=int(n/(10**i))
        n=n-dig*(10**i)
        sum_total=sum_total+dig
    print(sum_total)

#第二种办法 求余数
def digit_sum1(x):
    sum_total=0
    for i in range(len(str(x))):
        dig=x%10
        sum_total=sum_total+dig
        x=int(x/10)
    return sum_total

print("各个位数和为：{}".format(digit_sum1(11223345)))



def factorial(x):
    """
    求x的阶乘
    :param x: 
    :return: 
    """
    value=x
    for i in range(x-1,1,-1):
        value=value*i
    return(value)

print(factorial(6))

def is_prime(x):
    """
    判断x是否是质数
    :param x: 
    :return: 
    """
    flag=1
    for i in range(2,x):
        if(x%i==0):
            print("{}不是质数".format(x))
            flag=0
            break
    if(flag==1):
        print("{}是质数".format(x))

is_prime(677)


def reverse(text):
    newstr=""
    for index in range(len(text)-1,-1,-1):
        newstr=newstr+text[index]
    return newstr

print(reverse("abcdefg^$h1947"))


print(4321%1000)






