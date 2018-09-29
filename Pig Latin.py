


#思路：先考虑正常场景写完流程，再补充if语句覆盖异常情况。

testWord=input("请输入测试的单词：")

if(len(testWord)<=0):
    print("这不是一个合法的单词。")

elif(testWord.isalpha()==False):
    print("单词里面有其他字符。")

else:
    changeWord = testWord[1:] + testWord[0] + "ay"
    print("转换后的单词为：{}".format(changeWord.lower()))









