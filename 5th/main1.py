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

lasts = []
for seed in seeds:
    last = seed
    for stage in stages:
        # print("---", stage, "---" )
        for element in starts[stage]:
            # print(element)
            if last >= element[1] and last <= (element[1]+element[2]) :
                last = element[0] + (last - element[1])
                break
    lasts.append(last)
print(min(lasts))