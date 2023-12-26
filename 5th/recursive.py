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
        pairs.append((seed, seeds[i+1]+seed))

starts = []
count = -1
for i, line in enumerate(file):
    new_line = line.replace("\n", "")
    if ":" in new_line:
        start, _, finish = new_line.split(" ")[0].split("-")
        starts.append([])
        count += 1
    else:
        vals = new_line.split(" ")
        if (len(vals)<3): continue
        destination, source, rang = new_line.split(" ")
        starts[count].append((int(destination), int(source), int(rang)))

# fix the fact that there are multiple ranges inside a transform
stages = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
print(starts)
def recursive(seed_range, left):
    if left == len(stages):
        return min(seed_range)
    for pair in starts[left]:
        seed_start, seed_end = seed_range[0], seed_range[1]
        element_start, element_end = pair[1], pair[1] + pair[2]
        if (seed_end < element_start) or (seed_start > element_end): # seeds out of range
            return recursive(seed_range, left+1)
        if (seed_start > element_start and seed_end < element_end): # seeds totally included in range
            return recursive((pair[0] + (seed_start - element_start), (pair[0] + (seed_end - element_start))) ,left+1)
        if (seed_start < element_start and seed_end > element_end): # the range in totally included
            return min(
                recursive((seed_start, element_start-1), left+1),
                recursive((element_end + 1, seed_end), left+1),
                recursive((element_start, element_end), left+1),
            )
        if (seed_start < element_start and seed_end < element_end): # seeds start out left but end inside the range
            return min(
                recursive((seed_start, element_start-1), left+1),
                recursive((element_start, (pair[0] + (seed_end - element_start))), left+1),
            )
        else:
            return min(
                recursive((element_end+1, seed_end), left+1),
                recursive((pair[0] + (seed_start - element_start), element_end), left+1)
            )

mins = []
for pair in pairs:
    mins.append(recursive(pair, 0))

print(mins)
# from datetime import datetime
# minimum = 3169137700

# for pair in pairs:
#     a, b = pair[0], pair[0] + pair[1]
#     print(pair)
#     print("Current Time =", datetime.now().strftime("%H:%M:%S"))
#     for x in range(a, b+1):
#         if((b-x)%1000000 == 0): print(b-x, "Current Time =", datetime.now().strftime("%H:%M:%S"), minimum)
#         last = x
#         for stage in stages:
#             for element in starts[stage]:
#                 if last >= element[1] and last <= (element[1]+element[2]) :
#                     last = element[0] + (last - element[1])
#                     break
#         minimum = last if last < minimum else minimum
# print(minimum)
