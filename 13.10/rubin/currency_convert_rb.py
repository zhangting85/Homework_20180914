# -*-coding:utf-8-*-

import logging
import argparse
import sys


def mylogger(level, filename):
    logger = logging.getLogger()
    # 设置格式
    logger.setLevel(level)
    file_formatter = logging.Formatter(
        '%(asctime)s-%(pathname)s-[line:%(lineno)d]-%(levelname)s-%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    console_formatter = logging.Formatter('[line:%(lineno)d]-%(levelname)s-%(message)s')
    # 使用FileHandler输出到文件
    fh = logging.FileHandler(filename)
    fh.setFormatter(file_formatter)
    # 使用StreamHandler输出到控制台
    sh = logging.StreamHandler()
    sh.setFormatter(console_formatter)
    # 添加两个Handler
    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger


class CurrencyConvert(object):

    def __init__(self):

        parser = argparse.ArgumentParser(prog="currency_convert", fromfile_prefix_chars="<",
                                         usage="%(prog)s <--field N> [--multiplier N] [-i input] [-o output]")

        parser.add_argument("--field", metavar="N", required=True, type=int, help="价格信息在CSV的第N行需要进行转换")
        parser.add_argument("--multiplier", metavar="N", type=float, default=0.8, help="转换方法为把当前的数值乘以N，这个N表示汇率")
        parser.add_argument("-i", metavar="input", nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                            help="从input文件内读取CSV文件内容(或者从stdin读取)")
        parser.add_argument("-o", metavar="output", nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                            help="输出到output文件中(或者输出到stdout)")
        arguments = parser.parse_args()

        self.logger = mylogger(level=logging.DEBUG, filename="log.txt")

        self.field = arguments.field
        self.logger.info("self.field: %s" % self.field)

        self.multiplier = arguments.multiplier
        self.logger.info("self.multiplier: %s" % self.multiplier)

        self.data_file = arguments.i
        self.logger.info("self.data_file: %s" % self.data_file)

        self.output = arguments.o
        self.logger.info("self.output: %s" % self.output)

    def currency_convert_parser(self, input_file, output_file):
        """解析源文件每一行，汇率转换后，变成新的一行"""
        # 读取第一行，写入文件
        first_line = input_file.readline()
        output_file.write(first_line)
        self.logger.info("data.csv‘s first line: %s" % first_line)
        # 读取每一行，汇率转换，替换并写入文件
        for line in input_file.readlines():  # input_file.readlines()是一个字符串列表,先前有了readline直接从第二行开始读取
            currency_symbol_const = "€"
            comma = ','
            decimal_point_us = '.'
            decimal_point_eu = ','
            line_split_list = line.split(comma)
            price_origin = line_split_list[(self.field - 1)]
            if currency_symbol_const in line:
                price_origin = line_split_list[(self.field - 1)] + decimal_point_eu + line_split_list[self.field]
            price_update = price_origin
            self.logger.info("origin line: %s" % line)
            # 欧元转成美元的情况
            currency_symbol = "€"
            if currency_symbol in price_origin:
                price_update = price_origin[1:]
                price_update = price_update.replace(decimal_point_eu, decimal_point_us)
                currency_symbol = ""
            # 把价格提取处理，然后替换，写入新的文件
            price_target = currency_symbol + str(round(float(price_update) * self.multiplier, 2))
            if currency_symbol_const in price_target:
                price_target = price_target.replace(decimal_point_us, decimal_point_eu)
            new_line = line.replace(price_origin, price_target)
            self.logger.info("new_line: %s" % new_line)
            output_file.write(new_line)

    def currency_convert(self):
        """
        把data.csv文件从美元换算成欧元，输出data-fr.csv,并且可以换算回来
        """

        try:
            input_file = self.data_file
            output_file = self.output
            if self.data_file.isatty():
                self.data_file = input("Please enter the input file name: ")
                input_file = open(self.data_file, "r", encoding="utf-8")

            if self.output.isatty():
                self.output = input("Please enter the output file name: ")
                output_file = open(self.output, "w", encoding="utf-8")

            self.currency_convert_parser(input_file, output_file)

        except IOError as e:
            print(e)

        finally:
            output_file.close()
            input_file.close()


if __name__ == "__main__":
    # 测试用例
    test = CurrencyConvert()
    test.currency_convert()

