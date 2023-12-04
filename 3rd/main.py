file = open("input.txt", "r")


def isDigit(char):
    return char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

result = 0
i_MAX = 0
matrix = []
sol = []
max_j = 0


for line in file:
    new_line = line.replace("\n", "")
    matrix.append(list(new_line))
    max_j = len(list(new_line))
    temp_num = ""
    indexes = []
    indexes_to_check = []
    for j, char in enumerate(new_line):
        if isDigit(char):
            temp_num+=char
            indexes.append(str(i_MAX)+"+"+str(j))
            print(str(i_MAX)+"+"+str(j), char)
            if(j == max_j-1):
                if not temp_num == "":
                    for index in indexes:
                        ix, jx = index.split("+")
                        ix = int(ix)
                        jx = int(jx)
                        
                        if not str(ix)+"+"+str(jx-1) in indexes:
                            indexes_to_check.append(str(ix)+"+"+str(jx-1))
                        if not str(ix)+"+"+str(jx+1) in indexes:
                            indexes_to_check.append(str(ix)+"+"+str(jx+1))

                        indexes_to_check.append(str(ix-1)+"+"+str(jx))
                        indexes_to_check.append(str(ix+1)+"+"+str(jx))
                        indexes_to_check.append(str(ix-1)+"+"+str(jx-1))
                        indexes_to_check.append(str(ix-1)+"+"+str(jx+1))
                        indexes_to_check.append(str(ix+1)+"+"+str(jx-1))
                        indexes_to_check.append(str(ix+1)+"+"+str(jx+1))
                    sol.append((set(indexes_to_check), int(temp_num)))
                    print(set(indexes_to_check), int(temp_num))
                    indexes = []
                    indexes_to_check = []
                    temp_num = ""
        else:
            if not temp_num == "":
                for index in indexes:
                    ix, jx = index.split("+")
                    ix = int(ix)
                    jx = int(jx)
                    
                    if not str(ix)+"+"+str(jx-1) in indexes:
                        indexes_to_check.append(str(ix)+"+"+str(jx-1))
                    if not str(ix)+"+"+str(jx+1) in indexes:
                        indexes_to_check.append(str(ix)+"+"+str(jx+1))

                    indexes_to_check.append(str(ix-1)+"+"+str(jx))
                    indexes_to_check.append(str(ix+1)+"+"+str(jx))
                    indexes_to_check.append(str(ix-1)+"+"+str(jx-1))
                    indexes_to_check.append(str(ix-1)+"+"+str(jx+1))
                    indexes_to_check.append(str(ix+1)+"+"+str(jx-1))
                    indexes_to_check.append(str(ix+1)+"+"+str(jx+1))
                sol.append((set(indexes_to_check), int(temp_num)))
                print(set(indexes_to_check), int(temp_num))
                indexes = []
                indexes_to_check = []
                temp_num = ""
    i_MAX+=1
sum = 0
for indexes_to_check, num in sol:
    for index in indexes_to_check:
        i, j = index.split("+")
        i = int(i)
        j = int(j)
        if i >= 0 and j < max_j and j >= 0 and i < i_MAX:
            if not isDigit(matrix[i][j]) and matrix[i][j] != ".":
                print(i, j, ":", num)
                sum+=num
                break
        
print(sum)
