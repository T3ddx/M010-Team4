import xlrd

def getDict():
    workbook = xlrd.open_workbook("Team4-Table.xls")
    sheet = workbook.sheet_by_index(0)

    dict = {}

    for i in range(73):
        char = sheet.cell(i,0).value
        binary = sheet.cell(i,1).value

        dict[char] = binary

    return dict

charMap = getDict()

file_name = input("enter the name of the file to encode: ")
try:
    code_file = open(file_name)
    my_str = code_file.read()
    code_output = open("BinOutput.txt", "w+")

    result = ''
    bits = 0

    while len(my_str) > 0:
        add = charMap[my_str[0]]
        result+=add
        bits+=len(add)
        my_str = my_str[1:]

    code_output.write(str(bits) + "." + result)
except:
    print("No file named that.")

