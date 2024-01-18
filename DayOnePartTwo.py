numbers9 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbersA = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
numbers = {
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
}

def replace_words():
    count = 0
    changed_input_first = []
    changed_input_last = []
    number_seqs = []

    with open(
        "/Users/bigbird/Desktop/Python/Advent of Code/Day One/PuzzleInputD1P1.txt"
    ) as file:
        for line in file:
            input = line
            try:
                indices = [line.find(number) for number in numbersA]
                first_position = indices.index(min(index for index in indices if index > -1))
                first_num = numbersA[first_position]
                input_first = input.replace(first_num,numbers.get(first_num))
            except:
                input_first = input

            try:
                indices = [line.rfind(number) for number in numbersA]
                last_position = indices.index(max(index for index in indices if index > -1))
                last_num = numbersA[last_position]
                input_last = input.replace(last_num,numbers.get(last_num))
            except:
                input_last = input
            
            numbers_in_first_str = []
            numbers_in_last_str = []
            for char in input_first:
                if char in numbers9:
                    numbers_in_first_str.append(char)
            for char in input_last:
                if char in numbers9:
                    numbers_in_last_str.append(char)
            
            number_seqs.append(int(numbers_in_first_str[0] + numbers_in_last_str[-1]))

            #count = count + 1
            #if count == 100:
            #    break


 
        
        
            
        
            

    list_total = sum(number_seqs)
    list_count = len(number_seqs)
    print(number_seqs)
    print(list_total)
    print(list_count)

replace_words()