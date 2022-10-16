import xlrd

# function of dictionary
def dic():
    # open the Excel file and get the first sheet
    wb = xlrd.open_workbook("Team4-Table.xls")
    sh = wb.sheet_by_index(0)

    Bin2Char = {}

    # read all the characters and put them to the dictionary
    for i in range(0,73):
        char = sh.cell(i, 0).value
        binary = sh.cell(i, 1).value

        Bin2Char[binary] = char

    return Bin2Char

# assign the dictionary 
Bin2Char = dic()
file_name = input("enter the name of the file to decode: ")
# get the file name from user and read from it
file = open(file_name,"r")
binary = file.read()
result = ""
binary = str(binary.split(".")[1])

#5 short "1"      7 long "0"
# while loop run as long as there is still number in it
while binary!="":
    # determine if this part is short base on the beginning
    if binary[0] == "1":
        temp = Bin2Char[binary[0:5]]
        binary = binary[5:]
    # determine if this part is long base on the beginning
    elif binary[0] == "0":
        temp = Bin2Char[binary[0:7]]
        binary = binary[7:]

    result += temp

# open the output file and output the results
file_decode = open("TextOutput.txt","w")
file_decode.write(result)

