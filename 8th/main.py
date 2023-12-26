file = open("input.txt", "r")

actions = [x for x in file.readline().replace("\n", "")]
length = len(actions)

def roll_over_move(current_action):
    return current_action%length + 1

file.readline()
# print(actions)
nodes = {}
for line in file:
    new_line = line.replace("\n", "")
    node, dir = new_line.split(" = ")
    L, R = dir.replace("(", "").replace(")", "").split(", ")
    #print(node, L, R)
    nodes[node] = {"L": L, "R": R}

current_action = 1
number_of_actions = 0
final_node = "AAA"
while final_node != "ZZZ":
    final_node = nodes[final_node][actions[current_action-1]]
    number_of_actions += 1
    current_action = roll_over_move(current_action)
print(number_of_actions)