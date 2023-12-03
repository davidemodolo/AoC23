file = open("input.txt", "r")

ids = 0
power = 0
for line in file:
    new_line = line.replace("\n", "")
    game = new_line.split(":")
    id = game[0].split(" ")
    game_sets = game[1].split(";")
    # itsokay = True
    min_R, min_G, min_B = 0, 0, 0
    for set in game_sets:
        single_draws = set.split(", ")
        R, G, B = 0, 0, 0
        for draw in single_draws:
            components_of_draw = draw.split(" ")
            if("" in components_of_draw) : components_of_draw.remove("")
            if components_of_draw[1] == "red":
                R+=int(components_of_draw[0])
                if int(components_of_draw[0]) > min_R: min_R = int(components_of_draw[0])
            if components_of_draw[1] == "green":
                G+=int(components_of_draw[0])
                if int(components_of_draw[0]) > min_G: min_G = int(components_of_draw[0])
            if components_of_draw[1] == "blue":
                B+=int(components_of_draw[0])
                if int(components_of_draw[0]) > min_B: min_B = int(components_of_draw[0])
        # if not (R <= 12 and G <= 13 and B <= 14):
        #     itsokay = False
        #     break
    # if itsokay:
    #     ids+= int(id[1])
    power+=min_R*min_G*min_B
# print(ids)
print(power)