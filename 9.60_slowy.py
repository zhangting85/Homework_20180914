

#问题一：循环的时候往往不知道循环的边界。需要手动去算。或者跑一次再改。这种正常吗？
#问题二：一旦涉及到函数，常常变量的值不知道为什么传递不下去。

#常犯的问题：循环里面没有对变量做改动。导致每次循环开始时用的变量还是最初的原始值。得不到要的结果。

#连接字符串？？？？

def anti_vowel(text):
    vowellist=['a','e','i','u','o','A','E','I','U','O']
    s=""
    for i in range(len(text)):
        if(text[i] not in vowellist):
            s=s+text[i]
    return  s

print(anti_vowel("This is my family"))


def anti_vowel1(text):
    vowellist=['a','e','i','u','o','A','E','I','U','O']
    for i in text:
        if i in vowellist:
            text=text.replace(i,'')
    return text


print(anti_vowel1("This is bag"))



def scrabble_score(word):
    score={"a":1,"c":3,"b":3,"e":1,"d":2,"g":2,"f":4,"i":1,"h":4,"k":5,"j":8,"m":3}
    total=0
    for i in word:
        for key,value in score.items():
            if i.upper()==key.upper():
                total=total+value
                break
    return total

print(scrabble_score("aA"))



word="aaa"

text="This is back and back"

newlist=text.split("aaa")

print(newlist)


def censor(text,back):
    length=len(back)
    replaceword=length*'*'

    newlist=text.split(back)
    s=replaceword.join(newlist)

    return s


print(censor("This is back and back","back"))


def count(sequence,item):
    countt=0
    for i in sequence:
        if i==item:
            countt=countt+1
    return countt

print(count([1,[2],3,1,2],[2]))


def purify(numbers):
    list=[]
    for i in numbers:
        if(i%2==0):
            list.append(i)
    return list

print(purify([1,3,5,0,2]))


def product(numbers):
    s=1
    for i in numbers:
        s=s*i
    return s

print(product([1,2,4,5]))


def remove_duplicates(s):
    list=[]
    for i in s:
        if i not in list:
            list.append(i)

    return list

print(remove_duplicates([1,1,3,3,4]))


def median(x):
    newlist = x
    if (len(x) % 2==1):
        while (len(x) != 1):
            newlist.remove(max(newlist))
            newlist.remove(min(newlist))
        for i in newlist:
            return i

    else:
        while(len(x)!=2):
            newlist.remove(max(newlist))
            newlist.remove(min(newlist))
        total=0
        for i in newlist:
            total=total+i
        return total/2


print(median([1,2,3,4,5,6,7]))


















