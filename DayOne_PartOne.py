numbers9 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def find_first_last():
    count = 0
    number_seqs = []
    with open(
        "/Users/bigbird/Desktop/Python/Advent of Code/Day One/PuzzleInputD1P1.txt"
    ) as file:
        for line in file:
            numbers_in_str = []
            for char in line:
                if char in numbers9:
                    numbers_in_str.append(char)
            number_seqs.append(int(numbers_in_str[0] + numbers_in_str[-1]))
            #count = count + 1
            #if count == 10:
            #    break

    list_total = sum(number_seqs)
    print(number_seqs)
    print(list_total)

find_first_last()