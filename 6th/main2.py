from math import sqrt, floor, ceil
file = open("input.txt", "r")
def isNumber(x):
    try:
        int(x)
    except ValueError:
        return False
    return True

times = [int(x) for x in file.readline().split(":")[1].split(" ") if isNumber(x)]
distances = [int(x) for x in file.readline().split(":")[1].split(" ") if isNumber(x)]

final_time = ""
for element in times:
    final_time+=str(element)

final_distance = ""
for element in distances:
    final_distance+=str(element)

final_time = int(final_time)
final_distance = int(final_distance)


x1 = (-final_time+sqrt(final_time**2-4*(final_distance)))/2
x2 = (-final_time-sqrt(final_time**2-4*(final_distance)))/2
x1 = ceil(x1)
x2 = floor(x2)
print(x1-x2-1)