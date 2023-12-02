file = open("input.txt", "r")
def isDigit(char):
    return char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

spelled = [("nine", "9"),  ("eight", "8"), ("one", "1"), ("two", "2"),  ("seven", "7"), ("six", "6"), ("five", "5"), ("four", "4"), ("three", "3")]

sum = 0
for line in file:
    indexes = []
    # 1.1
    for i, char in enumerate(line):
        if isDigit(char):
            indexes.append((i, char))
    # indexes.sort()
    # sum+=(int(indexes[0][1]+indexes[len(indexes)-1][1]))
    # 1.2
    for spelled_digit in spelled:
        destroyable_line = line
        while spelled_digit[0] in destroyable_line:
            indexes.append((destroyable_line.find(spelled_digit[0]), spelled_digit[1]))
            destroyable_line_list = list(destroyable_line)
            for i in range(len(spelled_digit[0])):
                destroyable_line_list[destroyable_line.find(spelled_digit[0]) + i] = "x"
            destroyable_line = "".join(destroyable_line_list)

    indexes.sort()
    sum+=(int(indexes[0][1]+indexes[len(indexes)-1][1]))

print(sum)