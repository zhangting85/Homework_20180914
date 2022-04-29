# Pig Latin 翻译器

print("Pig Latin 翻译器")
original = input("请输入一个英文单词:")
pyg = 'ay'
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word+first+pyg
    new_word = new_word[1:]
    print(new_word)
    print(original)
else:
    print("输入的单词不合法")
