##函数中可以用exit吗？exit与return的区别？
##参考其它答案中：1.参数如何设置和获取？ 2.<>怎样作为参数标志 3. 欧元符号中的逗号 4. 输入输出到标准输入输出的方法 3.一些小点：文件打开时设置utf-8？
import argparse

parser = argparse.ArgumentParser('-f -m -i -o')
parser.add_argument("-f","--field", help="金额所在的字段位置",required=True)
parser.add_argument("-m","--multiplier", help="汇率",default=0.8)
parser.add_argument("-i", "--input",help="输入文件")
parser.add_argument("-o", "--output",help="输出文件")

my_args = parser.parse_args()
filed,multiplier,input_file,output_file=my_args.field,my_args.multiplier,my_args.input,my_args.output

def rate_trans(in_file_name,out_file_name,field,multiplier):
    if in_file_name==None:
          ##等待用户的多行输入不能直接换行
        with open('tmp.in','w',encoding='utf-8') as tmp_in:
            for line in input('pls input the content needed to be tranfrom:').split('#'):
                tmp_in.write(line+'\n')
        in_file_name='tmp.in'
    if out_file_name==None:
        out_file_name='tmp.out'

    field,multiplier =int(field),float(multiplier)

    in_file=open(in_file_name,encoding='utf-8')
    out_file=open(out_file_name,'w',encoding='utf-8')
    line_ind=0
    for line in in_file:
        if line_ind==0:
            trans_line=line
        else:
            words=line.split(',')
            if words[field][0]!='€':  ##
                words[field]='€'+str(round(float(words[field])*multiplier,2))
            else:
                words[field] =str(round(float(words[field][1:]) * multiplier, 2))

            trans_line=','.join(words)
        out_file.write(trans_line)
        line_ind+=1
    in_file.close()
    out_file.close()
    if in_file_name=='tmp.in':
        pass
    if out_file_name=='tmp.out':
        with open(out_file_name,encoding='utf-8') as out_file:
            for line in out_file:
                print(line,end='')  ##print不输出换行符的用法

if __name__=='__main__':
    rate_trans(input_file,output_file,filed,multiplier)
