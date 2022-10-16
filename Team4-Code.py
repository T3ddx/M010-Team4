import xlrd

#creates a dictionary from the excel table
def getDict():
    workbook = xlrd.open_workbook("Team4-Table.xls")
    sheet = workbook.sheet_by_index(0)

    dict = {}

    #iterates through the excel
    for i in range(73):
        char = sheet.cell(i,0).value
        binary = sheet.cell(i,1).value

        dict[char] = binary

    return dict

charMap = getDict()

#gets the file name the user is trying to encode
file_name = input("enter the name of the file to encode: ")
try:
    #gets the file and creates a new file named "BinOutput.txt"
    code_file = open(file_name)
    my_str = code_file.read()
    code_output = open("BinOutput.txt", "w+")

    result = ''
    bits = 0

    #while my_str still has characters, it iterates through and codes
    #each character. It gets the first character in string, converts
    #it using the dictionary and then adds it to the final string.
    while len(my_str) > 0:
        add = charMap[my_str[0]]
        result+=add
        bits+=len(add)
        my_str = my_str[1:]
    
    #writes to the the file "BinOutput.txt"
    code_output.write(str(bits) + "." + result)
except:
    #if it errors, it tells the user that they inputed the wrong file
    print("No file named that.")

