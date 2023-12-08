file = open("input.txt", "r")

def countPairs(hand):
    potential_pairs = {}
    for card in hand:
        if card in potential_pairs:
            potential_pairs[card] += 1
        else:
            potential_pairs[card] = 1
    return len([card for card in potential_pairs if potential_pairs[card] == 2])

def isOneTriple(hand):
    potential_triple = {}
    for card in hand:
        if card in potential_triple:
            potential_triple[card] += 1
        else:
            potential_triple[card] = 1
    return len([card for card in potential_triple if potential_triple[card] == 3])>0

def isFour(hand):
    potential_triple = {}
    for card in hand:
        if card in potential_triple:
            potential_triple[card] += 1
        else:
            potential_triple[card] = 1
    return len([card for card in potential_triple if potential_triple[card] == 4])>0

def getHandValue(hand):
    if len(set(hand)) == 1:
        return 7
    if len(set(hand)) == len(hand):
        return 1
    if isFour(hand):
        return 6
    if countPairs(hand) == 1 and isOneTriple(hand):
        return 5
    if isOneTriple(hand) and countPairs(hand) == 0:
        return 4
    if countPairs(hand) == 2:
        return 3
    if countPairs(hand) == 1:
        return 2

def getMaxFromJs(hand):
    best_hand = hand
    best_value = getHandValue(hand)
    for i in range(len([x for x in hand if x == "J"])+1):
        for card in cards:
            new_hand = hand.replace("J", card, i)
            val = getHandValue(new_hand)
            if val > best_value:
                best_hand = new_hand
                best_value = val
    return best_hand



values = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def compare(hand1, hand2):
    # remove the two ifs for 7.1
    if "J" in hand1[0]:
        val_1 = getHandValue(getMaxFromJs(hand1[0]))
    else:    val_1 = getHandValue(hand1[0])
    if "J" in hand2[0]:
        val_2 = getHandValue(getMaxFromJs(hand2[0]))
    else: val_2 = getHandValue(hand2[0])
    if  val_1 == val_2:
        for i in range(len(hand1[0])):
            card1 = values[hand1[0][i]] if hand1[0][i] in values else int(hand1[0][i])
            card2 = values[hand2[0][i]] if hand2[0][i] in values else int(hand2[0][i])
            if card1 != card2:
                 if card1 > card2:
                     return 1
                 else:
                     return -1
    if val_1 > val_2:
        return 1
    else:
        return -1
from functools import cmp_to_key
hands = []
for i, line in enumerate(file):
    new_line = line.replace("\n", "")
    hand, points = new_line.split(" ")
    hands.append((hand, int(points)))
    

hands = sorted(hands, key=cmp_to_key(compare))
val = 0
for i in range(len(hands)):
    val+=hands[i][1]*(i+1)

print(val)