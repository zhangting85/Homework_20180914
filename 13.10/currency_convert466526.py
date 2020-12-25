from decimal import Decimal

def get_two_float(f_str, n, fuhao1, fuhao2):
    f_str = str(f_str)  # f_str = '{}'.format(f_str) 也可以转换为字符串
    a, b, c = f_str.partition(fuhao1)
    c = (c + "0" * n)[:n]  # 如论传入的函数有几位小数，在字符串后面都添加n为小数0
    return fuhao2.join([a, c])

class Currency():
    '''需求：汇率转换,field = 价格所在列-1'''

    def __init__(self, field=1, multiplier=0.8, i="./data_in.csv", o='./data_out.csv'):
        self.field = field  #价格所在列-1
        self.multiplier = multiplier
        self.i = i
        self.o = o

    @property
    def r_file(self):
        with open(self.i,"r") as f:
            rd = f.readlines()
        return rd

    def w_file(self):
        rd = self.r_file
        for ind,i in enumerate(rd):
            rd[ind] = i.split(',')
            if ind != 0:
                new =eval(rd[ind][self.field])*self.multiplier
                rd[ind][self.field] = "€"+get_two_float(new, 2,'.', ',')
            rd[ind] = ','.join(rd[ind])
        rd = ','.join(rd)
        with open(self.o,'w',encoding='utf-8') as f_out:
            f_out.write(rd)

if __name__ == '__main__':
    Currency().w_file()
