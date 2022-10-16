import xlrd

def dic():
    wb = xlrd.open_workbook("Team4-Table.xls")
    sh = wb.sheet_by_index(0)

    Bin2Char = {}

    for i in range(0,73):
        char = sh.cell(i, 0).value
        binary = sh.cell(i, 1).value

        Bin2Char[binary] = char

    return Bin2Char

Bin2Char = dic()
file_name = input("enter the name of the file to decode: ")

file = open(file_name,"r")
binary = file.read()
result = ""
binary = str(binary.split(".")[1])

#5 short "1"      7 long "0"
while binary!="":
    if binary[0] == "1":
        temp = Bin2Char[binary[0:5]]
        binary = binary[5:]

    elif binary[0] == "0":
        temp = Bin2Char[binary[0:7]]
        binary = binary[7:]

    result += temp

file_decode = open("TextOutput.txt","w")
file_decode.write(result)

