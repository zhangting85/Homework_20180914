# coding=utf-8
from __future__ import print_function

import _io
import sys, argparse, os

parser = argparse.ArgumentParser(description='currency_convert', prog="currency_convert",
                                 usage="%(prog)s <--field N> [--multiplier N] [-i input] [-o output]")

parser.add_argument("--field", metavar="N", required=True, help="价格信息在CSV的第N行需要进行转换")
parser.add_argument("--multiplier", metavar="N", help="转换方法为把当前的数值乘以N，这个N表示汇率")
parser.add_argument("-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help="从input文件内读取CSV文件内容(或者从stdin读取)")
parser.add_argument("-o", nargs='?', default=sys.stdout, help="输出到output文件中(或者输出到stdout)")
parser.add_argument("-l", required=False, nargs='?', default=sys.stdin,
                    help="请输如货币符号，默认欧元")

args = parser.parse_args()
field = args.field
multiplier = args.multiplier
input_i = args.i
output = args.o
letter = args.l


def read_csv(input_data, type_name):
    text = []
    if type_name != 'str':
        open_file = open(input_data, "r")

        info_open = open_file.readlines()
        for each_line in info_open:
            line = each_line.split(",")
            text.append(line)

        open_file.close()
        return text
    else:
        line = input_data.split(",")
        text.append(line)
        return text


def deal_data(data, field, multiplier, letter):
    temp = round(float(data[int(field - 1)]) * float(multiplier), 2)
    a = ''
    h = ','

    if letter != '€':
        h = '.'

    while int(temp) != 0:
        if temp >= 1000:
            a = h + str(round(temp % 1000, 2)) + a
        else:
            a = h + str(temp) + a

        temp = int(temp / 1000)

    if field == 2:
        return letter + str(a)[1:]
    return str(a)[1:]


def get_file():
    if isinstance(input_i, _io.TextIOWrapper):
        base_dir = os.getcwd()
        file_path = os.path.join(base_dir, '', 'data.csv')
        return read_csv(file_path, '')
    elif str(input_i).endswith(".csv"):
        return read_csv(input_i, '')
    elif isinstance(input_i, str):
        return read_csv(input_i, 'str')


def export_file(data):
    if isinstance(output, _io.TextIOWrapper):
        for e in data:
            for i in range(len(e)):
                if i == len(e) - 1:
                    print(e[i], end='')
                else:
                    print(e[i] + ',', end='')
        return
    else:
        open_file = open(output, "w")
        for e in data:
            for i in range(len(e)):
                if i == len(e) - 1:
                    open_file.write(e[i])
                else:
                    open_file.write(e[i] + ',')

        open_file.close()


if __name__ == '__main__':
    if isinstance(letter, _io.TextIOWrapper):
        letter = '€'
    data = get_file()

    for item in data[1:]:
        item[int(field) - 1] = deal_data(item, int(field), float(multiplier), letter)
    export_file(data)
