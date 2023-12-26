file = open("input.txt", "r")

actions = [x for x in file.readline().replace("\n", "")]
length = len(actions)

def roll_over_move(current_action):
    return current_action%length + 1

file.readline()
# print(actions)
nodes = {}
starting_nodes = []
for line in file:
    new_line = line.replace("\n", "")
    node, dir = new_line.split(" = ")
    L, R = dir.replace("(", "").replace(")", "").split(", ")
    # print(node, L, R)
    nodes[node] = {"L": L, "R": R}
    if node[2] == "A":
        starting_nodes.append(node)
# print(nodes)
starting = [x for x in starting_nodes]
current_action = 1
number_of_actions = 0
length_start_nodes = len(starting_nodes)
max_zed = 0
indexes = {}
while True:
    number_of_zed = 0
    for i in range(length_start_nodes):
        starting_nodes[i] = nodes[starting_nodes[i]][actions[current_action-1]]
        if starting_nodes[i][2] == "Z" and i not in indexes:
            print(f"[{i}] {starting[i]} - {starting_nodes[i]} - {number_of_actions +1}")
            indexes[i] = number_of_actions +1
    number_of_actions += 1
    current_action = roll_over_move(current_action)
    if len(indexes) == len(starting_nodes):
        break
print(indexes)
from math import lcm
string = ""
for element in indexes:
    string+=f"{indexes[element]}, "
eval(f"print(lcm({string}))")