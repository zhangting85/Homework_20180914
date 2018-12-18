import argparse
import sys
import io

'''
Class CurrencyConvert with 4 attributes field, multiplier, i(input), o(output) and methods as required.
'''
class CurrencyConvert():

    '''
    Function: by using argparse to add 4 arguments field, multiplier, i, o to __init__ function
    and to parse 4 arguments either from console or stdin/stdout.
    '''
    def __init__(self):

        parser = argparse.ArgumentParser(prog="currency_convert",
                                         usage="%(prog)s <--field N> [--multiplier N] [-i input] [-o output]")

        parser.add_argument("--field", required=True, help="价格信息在CSV的第N行需要进行转换")
        parser.add_argument("--multiplier", default= 0.8, help="转换方法为把当前的数值乘以N，这个N表示汇率")
        parser.add_argument("-i", nargs="?", default=sys.stdin, help="从input文件内读取CSV文件内容(或者从stdin读取)")
        parser.add_argument("-o", nargs="?", default=sys.stdout, help="输出到output文件中(或者输出到stdout)")

        arguments = parser.parse_args()

        self.field = arguments.field
        self.multiplier = arguments.multiplier
        self.i = arguments.i
        self.o = arguments.o

    '''
    One argument: the current line from the input file
    Return: the element of the list amount regarding input value field
    Function: get the USD amount text line, split line by comma, use the field number minus 1 to get the actual usd 
    value element.
    '''
    def get_the_usd_amount(self, line):
        amount = line.split(",")
        return amount[int(self.field) - 1]

    '''
    One argument: the current line from the input file
    Return: combination of two elements of the list amount regarding input value field
    Function: get the Euro amount text line, split line by comma, use the field number minus 1 and the field number 
    combination to get the actual eur value element by deleting the euro symbol and replacing the comma with dot
    '''
    def get_the_eur_amount(self, line):
        amount = line.split(",")
        print(amount[int(self.field) - 1].replace("€", "") + "." + amount[int(self.field)])
        return amount[int(self.field) - 1].replace("€", "") + "." + amount[int(self.field)]

    '''
    One argument: amount, the usd amount from function get_the_usd_amount()
    Return: the eur amount with an euro symbol, replace the dot with comma between digits
    Function: get the usd amount times the multiplier with 2 decimal points
    '''
    def convert_to_eur(self, amount):
        euro = round(float(amount) * float(self.multiplier), 2)
        return "€" + str(euro).replace(".", ",")

    '''
    One argument: amount, the eur amount from function get_the_eur_amount()
    Return: the usd amount, replace the comma with dot between digits
    Function: get the eur amount times the multiplier with 2 decimal points
    '''
    def convert_to_usd(self, amount):
        usd = round(float(amount) / float(self.multiplier), 2)
        return str(usd)

    '''
    One argument: text_name
    Return: new text that replaces the usd by the eur
    Function: read line by line from the text and replace the usd by the euro, 
    if there is no usd value, it just copies the line
    '''
    def read_file(self, text_name):
        newline = ""
        for line in text_name:
            try:
                newline += line.replace(self.get_the_usd_amount(line),
                                        self.convert_to_eur(float(self.get_the_usd_amount(line))))
            except ValueError:
                newline += line
        return newline

    '''
    Function: if the input/output is TTY, screen prints tips to let user enter the arguments
    if the input/output is redirection, it reads from the console
    if the input/output is with arguments, it reads from the arguments
    From read_file gets the new text then export it
    '''
    def usd_eur_file_export(self):
        new_text = ""
        if isinstance(self.i, io.TextIOWrapper):
            if self.i.isatty():
                self.i = input("Please enter the input file name: ")
                self.o = input("Please enter the output file name: ")
                with open(self.i, "r", encoding="utf-8") as text:
                    new_text = self.read_file(text)
            else:
                new_text = self.read_file(self.i)

        elif isinstance(self.i, str):
            with open(self.i, "r", encoding="utf-8") as text:
                new_text = self.read_file(text)

        if isinstance(self.o, io.TextIOWrapper):
            self.o = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            self.o.write(new_text)
        else:
            with open(self.o, "w", encoding="utf-8") as text2:
                text2.write(new_text)

    #usd file export
    def eur_usd_file_export(self):
        pass
'''
Create a CurrencyConvert instance usdeur, 
call the function usd_eur_file_export() to covert usd to eur
'''
if __name__ == '__main__':

    usdeur = CurrencyConvert()
    usdeur.usd_eur_file_export()

    #similar function as usd to eur
    #usdeur.eur_usd_file_export()
