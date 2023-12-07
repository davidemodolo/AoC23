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

tot = 1
for i in range(len(times)):
    x1 = (-times[i]+sqrt(times[i]**2-4*(distances[i])))/2
    x2 = (-times[i]-sqrt(times[i]**2-4*(distances[i])))/2
    x1 = ceil(x1)
    x2 = floor(x2)
    tot*=(x1-x2-1)

print(tot)