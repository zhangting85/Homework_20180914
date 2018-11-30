import argparse
import sys
import io

class CurrencyConvert():

    def __init__(self):
        #get arguments
        parser = argparse.ArgumentParser(prog="currency_convert",
                                         usage="%(prog)s <--field N> [--multiplier N] [-i input] [-o output]")

        parser.add_argument("--field", required=True, help="价格信息在CSV的第N行需要进行转换")
        parser.add_argument("--multiplier", default= 0.8, help="转换方法为把当前的数值乘以N，这个N表示汇率")
        parser.add_argument("-i", nargs="?", default=sys.stdin, help="从input文件内读取CSV文件内容(或者从stdin读取)")
        parser.add_argument("-o", nargs="?", default=sys.stdout, help="输出到output文件中(或者输出到stdout)")

        arguments = parser.parse_args()

        self.field = arguments.field
        self.rate = arguments.multiplier
        self.inputf = arguments.i
        self.outputf = arguments.o

    #get the usd amount
    def get_the_usd_amount(self, line):
        amount = line.split(",")
        return amount[int(self.field) - 1]

    #get the eur part
    def get_the_eur_part(self, line):
        part = line.split(",")
        print(part[int(self.field) - 1] + "," + part[int(self.field)])
        return part[int(self.field) - 1] + "," + part[int(self.field)]

    #get the eur amount
    def get_the_eur_amount(self, line):
        amount = line.split(",")
        print(amount[int(self.field) - 1].replace("€", "") + "." + amount[int(self.field)])
        return amount[int(self.field) - 1].replace("€", "") + "." + amount[int(self.field)]

    #convert to eur
    def convert_to_eur(self, amount):
        euro = round(float(amount) * float(self.rate), 2)
        return "€" + str(euro).replace(".", ",")

    #convert to usd
    def convert_to_usd(self, amount):
        euro = round(float(amount) / float(self.rate), 2)
        return str(euro)

    #read file into memory
    def read_file(self, text_name):
        newline = ""
        for line in text_name:
            try:
                newline += line.replace(self.get_the_usd_amount(line),
                                        self.convert_to_eur(float(self.get_the_usd_amount(line))))
            except ValueError:
                newline += line
        return newline

    #eur file export
    def usd_eur_file_export(self):
        new_text = ""
        if isinstance(self.inputf, io.TextIOWrapper):
            if self.inputf.isatty():
                self.inputf = input("Please enter the input file name: ")
                self.outputf = input("Please enter the output file name: ")
                with open(self.inputf, "r") as text:
                    new_text = self.read_file(text)
            else:
                new_text = self.read_file(self.inputf)
        elif isinstance(self.inputf, str):
            with open(self.inputf, "r") as text:
                new_text = self.read_file(text)

        if isinstance(self.outputf, io.TextIOWrapper):
            self.outputf.write(new_text)
        else:
            with open(self.outputf, "w") as text2:
                text2.write(new_text)

    #usd file export
    def eur_usd_file_export(self):
        pass

if __name__ == '__main__':

    usdeur = CurrencyConvert()
    usdeur.usd_eur_file_export()
    #usdeur.eur_usd_file_export()












