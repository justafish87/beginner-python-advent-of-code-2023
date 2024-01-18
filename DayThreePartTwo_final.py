import re
import numpy

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
        # print(file_input)


def number_find(row_num, column_num):
    gear_numbers = []
    gear_check = False
    gear_num = ""
    #check 3 by 7 grid around * for numbers
    for row_change in range(-1, 2):
        gear_num = ""
        gear_check = False
        for column_change in range(-3, 4):
            char = file_input[row_num + row_change][column_num + column_change]
            if char in numbers9:
                #build full number
                gear_num = gear_num + char
                # check whether * is one away from char and set a checker
                if column_change in range(-1, 2):
                    gear_check = True
                #deal with cases where it is the end of the row of 7 and char is in numbers9
                if column_change == 3:
                    if gear_check is True:
                        gear_numbers.append(int(gear_num))
                        gear_num = ""
                        gear_check = False
                    else:
                        gear_num = ""
            else:
                if gear_check is True:
                    gear_numbers.append(int(gear_num))
                    gear_num = ""
                    gear_check = False
                else:
                    gear_num = ""
    #create gear ratio for this * and add to global list
    if len(gear_numbers) > 1:
        gear = numpy.prod(gear_numbers)
        gear_ratios.append(gear)
        #create list to show numbers going into the ratio for troubleshooting
        check_gears.append(gear_numbers)
        gear_numbers = []
        gear_check = False
    else:
        gear_numbers = []
        gear_check = False


def main():
    bring_in_file()

    global check_gears
    check_gears = []
    global row_length
    row_length = len(file_input[0])
    global column_length
    column_length = len(file_input)
    print(row_length)
    print(column_length)

    global gear_ratios
    gear_ratios = []

    #find *'s and run numberfind function to get gear ratio
    row_num = 0
    for row in file_input:
        column_num = 0
        for column in row:
            if column == "*":
                number_find(row_num, column_num)
            column_num = column_num + 1
        row_num = row_num + 1
    print(check_gears)
    total_ratio = sum(gear_ratios)
    print(total_ratio)


main()
