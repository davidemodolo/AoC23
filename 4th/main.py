file = open("input.txt", "r")

sum = 0
dictionary = {}
for i, line in enumerate(file):
    if i in dictionary: dictionary[i]+=1
    else: dictionary[i] = 1
    new_line = line.replace("\n", "")
    card = new_line.split(":")
    winning_numbers, your_numbers = card[1].split("|")
    winning_numbers = [int(x) for x in winning_numbers.split(" ") if x != ""]
    your_numbers = [int(x) for x in your_numbers.split(" ") if x != ""]
    your_winning_numbers = [x for x in your_numbers if x in winning_numbers]
    length = len(your_winning_numbers)
    for j in range(length):
        index = i+j+1
        if index in dictionary: dictionary[index]+=dictionary[i]
        else: dictionary[index]=dictionary[i]
for i, e in enumerate(dictionary):
    if e != len(dictionary):
        sum+=dictionary[e]
print(sum)