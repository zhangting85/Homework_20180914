import re
print('欢迎使用我开发的转换器，请将转换器和要被处理的csv文件放在相同路径下，不然我无法为您工作，谢谢您的理解和支持！')

def currency(fileNum, Mul, fileName, outName):
    '''

    :param fileNum: 需要处理的文件的第几列
    :param Mul: 转换的汇率
    :param fileName: 需要处理的文件
    :param outName: 处理后重新输出的新文件名
    :return: 会自动生成outName的文件名，在当前文件夹中查找
    '''
    f = open(fileName, 'r', encoding='utf-8')
    f2 = open(outName, 'a',encoding='utf-8')
    n = 0
    count = 0

    while f.readline():
        n += 1
    f.close()
    f1 = open(fileName, 'r', encoding='utf-8')
    while count < n:
        if count == 0:
            f2.write(f1.readline())
            count += 1
        else:
            list_f1_change = ''
            list_f1 = f1.readline().split(',')
            list_f1[fileNum - 1] = '€' + str(float(list_f1[fileNum - 1]) * Mul)
            for i in range(0, len(list_f1) - 1):
                list_f1_change = list_f1_change + list_f1[i] + ','
            list_f1_change = list_f1_change + list_f1[len(list_f1) - 1]
            f2.write(list_f1_change)
            count += 1
    f1.close()
    f2.close()
    print('已处理完成，可到本目录下查找处理完成的csv文件！')
    f_out = open(outName, 'r', encoding='utf-8')
    s_user = f_out.read()
    print(s_user)
    f_out.close()
    return(s_user)

while True:
    user_input = input('请--help查看本工具的使用方法 或者直接按照要求输入:')
    user_data = {'filed': 2, 'multiplier': 0.8, 'input_file': '', 'output_filename': 'data-fr.csv'}
    if user_input == '--help':
        print('usage: current_covert < --field N > [ --multiplier N ] [ -i input ] [ -o output ]')
        print('''
           --field N 必填项，价格信息在CSV的第N列，需要进行转换。
           --multiplier N 选填项，转换方法为把当前的数值乘以N 这个N表示汇率
           -i input 从input 文件内读取CSV文件内容（或者从stdin输入）
           -o output 输出到out文件中（或者从输出到stout）
           eg: 
           >currency_convert --filed 2 --multiplier 0.8 -i data.csv -o data-fr.csv
        ''')
    else:
        s = user_input.split(' ')
        print(s)
        user_data['filed'] = s[s.index('--filed') + 1]
        if '--multiplier' in s:
            user_data['multiplier'] = s[s.index('--multiplier') + 1]
        if '-i' in s:
            user_data['input_file'] = s[s.index('-i') + 1]
        if '-o' in s:
            user_data['output_filename'] = s[s.index('-o') + 1]
        if '<.>' in s:
            user_data['input_file'] = s[1:-1]
        if user_data['input_file'] == '':
             user_text = input('请输入你要转换的内容：')
             user_f = open('data.csv', 'w+', encoding='utf-8')
             user_f.write(user_text)
             user_f.close()
             user_data['input_file'] = 'data.csv'
        if user_data['output_filename'] == '':
            if s[-1].endswith('.csv'):
                user_data['output_filename'] = s[-1]
            else:
                currency_output = currency(int(user_data['filed']), float(user_data['multiplier']), user_data['input_file'], user_data['output_filename'])
                print(currency_output)
                break
        currency(int(user_data['filed']), float(user_data['multiplier']), user_data['input_file'], user_data['output_filename'])
        break





