#Advent of Code 2023
#Day 8
#Jason R Evarts

def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def buildMap(data):
    buildMap = {}
    for line in data:
        key,value = line.split("=")
        value = value.replace("(","")
        value = value.replace(")","")
        value = value.strip()
        value = value.replace(" ", "")
        value = value.split(",")
        key = key.strip()
        buildMap[key] = value
    return buildMap

def main():
    file = ("day8testdata.txt")
    data = importData(file)
    mapDict = buildMap(data[2:])
    directions = data[0]
    directions = directions.replace("\n","")
    moving = True
    current_pos = "AAA"
    total_moves = 0
    while moving:
        for char in directions:
            if char == "L":
                possible_pos = mapDict.get(current_pos)
                current_pos = possible_pos[0]
                total_moves += 1
            else:
                possible_pos = mapDict.get(current_pos)
                current_pos = possible_pos[1]
                total_moves += 1
            if current_pos == "ZZZ":
                moving = False
                break
    print("Total Moves: ", total_moves)



def mainB():
    file = ("day8data.txt")
    data = importData(file)
    mapDict = buildMap(data[2:])
    directions = data[0]
    directions = directions.replace("\n","")
    print (directions)
    moving = True
    current_loc = []
    final_loc = []
    total_moves = 0
    final_loc_count = 0
    for key in mapDict.keys():
        if key[-1] == "A":
            current_loc.append(key)
        elif key[-1] == "Z":
            final_loc.append(key)
    while moving:
        for char in directions:
            if char == "L":
                for i in range(len(current_loc)):
                    possible_pos = mapDict.get(current_loc[i])
                    current_loc[i] = possible_pos[0]
            elif char == "R":
                for i in range(len(current_loc)):
                    possible_pos = mapDict.get(current_loc[i])
                    current_loc[i] = possible_pos[1]
            else:
                print ("Character not L or R: ", char)
            total_moves += 1
            for key in current_loc:
                if key[-1] == "Z":
                    #print (current_loc)
                    final_loc_count += 1
                else:
                    break
                if final_loc_count > 4:
                    print ("Almost at all locations: ", final_loc_count)
            if final_loc_count == len(current_loc):
                moving = False
                break
            else:
                final_loc_count = 0
    print("Total Moves: ", total_moves)


mainB()