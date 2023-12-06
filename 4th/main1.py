file = open("input2.txt", "r")

sum = 0
for line in file:
    new_line = line.replace("\n", "")
    card = new_line.split(":")
    winning_numbers, your_numbers = card[1].split("|")
    winning_numbers = [int(x) for x in winning_numbers.split(" ") if x != ""]
    your_numbers = [int(x) for x in your_numbers.split(" ") if x != ""]
    your_winning_numbers = [x for x in your_numbers if x in winning_numbers]
    if len(your_winning_numbers) > 0:
        sum+=2**(len(your_winning_numbers)-1)
print(sum)    