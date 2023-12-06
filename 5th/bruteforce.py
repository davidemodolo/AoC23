# opened 10 VS Code instances and run each instance on one range (bruteforce in 4D)
file = open("input.txt", "r")

def isNumber(x):
    try:
        int(x)
    except ValueError:
        return False
    return True


seeds = [int(x) for x in file.readline().split(":")[1].split(" ") if isNumber(x)]
pairs = []
for i, seed in enumerate(seeds):
    if i%2 == 0 and i != len(seeds)-1:
        pairs.append((seed, seeds[i+1]))
print(pairs)

starts = {}
last_start = ""
for i, line in enumerate(file):
    new_line = line.replace("\n", "")
    if ":" in new_line:
        start, _, finish = new_line.split(" ")[0].split("-")
        starts[finish] = []
        last_start = finish
    else:
        vals = new_line.split(" ")
        if (len(vals)<3): continue
        destination, source, rang = new_line.split(" ")
        starts[last_start].append((int(destination), int(source), int(rang)))
        
stages = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

def rabbit(hole):
    for stage in stages:
        # print("---", stage, "---" )
        for element in starts[stage]:
            # print(element)
            if last >= element[1] and last <= (element[1]+element[2]) :
                last = element[0] + (last - element[1])
                break
    return last

from datetime import datetime
minimum = 3169137700

for pair in pairs:
    a, b = pair[0], pair[0] + pair[1]
    print(pair)
    print("Current Time =", datetime.now().strftime("%H:%M:%S"))
    for x in range(a, b+1):
        if((b-x)%1000000 == 0): print(b-x, "Current Time =", datetime.now().strftime("%H:%M:%S"), minimum)
        last = x
        for stage in stages:
            for element in starts[stage]:
                if last >= element[1] and last <= (element[1]+element[2]) :
                    last = element[0] + (last - element[1])
                    break
        minimum = last if last < minimum else minimum
print(minimum)
