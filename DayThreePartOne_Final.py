import re

numbers9 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
non_spec_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]


def bring_in_file():
    global file_input
    file_input = []
    with open(
        "/Users/bigbird/Desktop/Python/Advent of Code/Day Three/PuzzleInputD3.txt"
    ) as file:
        # loop through the data
        for line in file:
            line = line.rstrip("\n")
            line_chars = []
            for char in line:
                if char != "\\":
                    line_chars.append(char)
                else:
                    break
            file_input.append(line_chars)


def check_special_char(row_position, row_change, column_position, column_change):
    #retrieves char at a certain position near number and adds to list
    try:
        spec_char_check.append(
            file_input[row_position + row_change][column_position + column_change]
        )
    except:
        spec_char_check.append(".")

def add_number(char_list,digit_temp):
    #check whether number is near any special characters and adds to final list if it is
    check = True
    char_in_list = (
        char in non_spec_characters for char in char_list
    )
    if all(char_in_list):
        check = False
    if digit_temp != "" and check is True:
        digit_temp = int(digit_temp)
        number_list.append(digit_temp)
    char_list = []

# main programme
def main():
    bring_in_file()
    global row_length
    row_length = len(file_input[0])
    global column_length
    column_length = len(file_input)

    row_num = 0
    global number_list
    number_list = []
    for row in file_input:
        digit = ""
        column_num = 0
        global spec_char_check
        spec_char_check = []
        for column in row:
            if column in numbers9:
                digit = digit + column
                print(digit)

                for row_change in range(-1, 2):
                    for col_change in range(-1, 2):
                        check_special_char(row_num, row_change, column_num, col_change)

                if (column_num == column_length - 1):  # to capture instances where last char of row is a number
                    add_number(spec_char_check, digit)
                    digit = ""
                    spec_char_check = []
            else:
                add_number(spec_char_check, digit)
                digit = ""
                spec_char_check = []
            column_num = column_num + 1
        row_num = row_num + 1
    #print(number_list)
    total_gears = sum(number_list)
    print(total_gears)


# call main programme
main()
