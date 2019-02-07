# -*- coding:utf-8 -*-：
import argparse
parser=argparse.ArgumentParser(description='')
parser.add_argument('--field',help='金额在第几列',choices=list(range(10)),type=int)#required=True,
parser.add_argument('--multiplier',help='汇率',default=0.8,type=float)
parser.add_argument('-i',help='需要转换的CSV文件',type=argparse.FileType('r'),dest='ori')
parser.add_argument('-o',help='转换后的CSV文件',type=argparse.FileType('w'),dest='proce')
args=parser.parse_args()
#定义用于io文件形式的类
class Csv(object):
    # 解析输出文件名
    m = str(args.proce)
    m = m.split('\'', args.field)
    m = m[1]
    def __init__(self):
        #存储表头
        i=0
        for r in args.ori:
            if i==0:
                with open(self.m, 'a+') as f:
                    f.write(r)
            else:
                s = r.split(',', args.field)
                t = s[args.field-1]
                tt=float(t)
                tt*=0.8
                nt=round(tt,2)
                nt=str(nt).replace('.',',')
                nt='"'+'€'+nt+'"'
                rr=r.replace(t,nt)
                with open(self.m,'a+',encoding='utf-8') as f:
                    f.write(rr)
            i+=1

#定义用于用户输入屏幕输出形式的类
class Csv1(object):
    def __init__(self):
        proce=[]
        csvhead=input('请输入表头数据：\n')
        proce.append(csvhead)
        while True:
            ori= input('请依次输入每行数据：\n')
            if ori!='over':
                s = ori.split(',', args.field)
                t = s[args.field - 1]
                tt = float(t)
                tt *= 0.8
                nt = round(tt, 2)
                nt = str(nt).replace('.', ',')
                nt = '"' + '€' + nt + '"'
                rr = ori.replace(t, nt)
                proce.append(rr)
            else:
                break
        for i in proce:
            print(i)
#根据命令行参数决定要用哪个类创建对象
if args.ori==None and args.proce==None:
    csv=Csv1()
else:
    csv=Csv()











