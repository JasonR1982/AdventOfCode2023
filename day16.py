#Advent of Code 2023
#Day 16
#Jason R Evarts
import itertools
def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def traceRoute(data, row, column, direction, active_map, direction_map):
    row = int(row)
    column = int(column)
    while True:
        if row < 0:
            return 1
        if row == len(data):
            return 1
        if column < 0:
            return 1
        if column == len(data[row]):
            return 1
        active_map[row] = active_map[row][:column]+"#"+active_map[row][column+1:]
        if direction == "n":
            if direction_map[row][column][0] == "^":
                break
            else:
                direction_map[row][column] = "^" + direction_map[row][column][1:]
            if data[row][column] == ".":
                data[row] = data[row][:column]+"^"+data[row][column+1:]
                row = row - 1
            elif data[row][column] == "^":
                break
            elif data[row][column] in ["|", ">", "<", "v"]:
                row = row - 1
            elif data[row][column] == "-":
                traceRoute(data, row, column-1, "w", active_map, direction_map)
                traceRoute(data, row, column+1, "e", active_map, direction_map)
                break
            elif data[row][column] == "\\":
                direction = "w"
                column = column - 1
            elif data[row][column] == "/":
                direction = "e"
                column = column + 1
            else:
                print ("Unhandled map element in \"N\"")
                return -1
        elif direction == "s":
            if direction_map[row][column][1] == "v":
                break
            else:
                direction_map[row][column] = direction_map[row][column][0] + "v" + direction_map[row][column][2:]
            if data[row][column] == ".":
                data[row] = data[row][:column]+"v"+data[row][column+1:]
                row = row + 1
            elif data[row][column] == "v":
                break
            elif data[row][column] in ["|", ">", "<", "^"]:
                row = row + 1
            elif data[row][column] == "-":
                traceRoute(data, row, column-1, "w", active_map, direction_map)
                traceRoute(data, row, column+1, "e", active_map, direction_map)
                break
            elif data[row][column] == "\\":
                direction = "e"
                column = column + 1
            elif data[row][column] == "/":
                direction = "w"
                column = column - 1
            else:
                print ("Unhandled map element in \"S\"")
                return -1
        elif direction == "e":
            if direction_map[row][column][2] == ">":
                break
            else:
                direction_map[row][column] = direction_map[row][column][:2] + ">" + direction_map[row][column][3]
            if data[row][column] == ".":
                data[row] = data[row][:column]+">"+data[row][column+1:]
                column = column + 1
            elif data[row][column] == ">":
                break
            elif data[row][column] in ["-", "^", "<", "v"]:
                column = column + 1
            elif data[row][column] == "|":
                traceRoute(data, row+1, column, "s", active_map, direction_map)
                traceRoute(data, row-1, column, "n", active_map, direction_map)
                break
            elif data[row][column] == "\\":
                direction = "s"
                row = row + 1
            elif data[row][column] == "/":
                direction = "n"
                row = row - 1
            else:
                print ("Unhandled map element in \"E\"")
                return -1
        elif direction == "w":
            if direction_map[row][column][3] == "<":
                break
            else:
                direction_map[row][column] = direction_map[row][column][:3] + "<"
            if data[row][column] == ".":
                data[row] = data[row][:column]+"<"+data[row][column+1:]
                column = column - 1
            elif data[row][column] == "<":
                break
            elif data[row][column] in ["-", "^", ">", "v"]:
                column = column - 1
            elif data[row][column] == "|":
                traceRoute(data, row+1, column, "s", active_map, direction_map)
                traceRoute(data, row-1, column, "n", active_map, direction_map)
                break
            elif data[row][column] == "\\":
                direction = "n"
                row = row - 1
            elif data[row][column] == "/":
                direction = "s"
                row = row + 1
            else:
                print ("Unhandled map element in \"W\"")
                return -1


def main():
    file = ("day16data.txt")
    data = importData(file)
    clean_data = []
    active_tiles = []
    direction_map = []
    running_total = 0
    for line in data:
        line = line.strip()
        active_line = ""
        direction_line = []
        for char in line:
            active_line = active_line +"."
            direction_line.append("....")
        clean_data.append(line)
        active_tiles.append(active_line)
        direction_map.append(direction_line)
    traceRoute(clean_data, 0,0,"e", active_tiles, direction_map)
    #Count the energized tiles
    row = 0
    #for line in clean_data:
    #    print (line)
    for line in active_tiles:
        running_total += line.count("#")
    print ("Total Energized Tiles Part A: ", running_total)

    max_tiles = 0
    for i in range(len(data)):
        active_tiles = []
        clean_data = []
        direction_map = []
        for line in data:
            line = line.strip()
            active_line = ""
            direction_line = []
            for char in line:
                active_line = active_line + "."
                direction_line.append("....")
            clean_data.append(line)
            active_tiles.append(active_line)
            direction_map.append(direction_line)
        direction = "e"
        traceRoute(clean_data, int(i), 0, direction, active_tiles, direction_map)
        running_total = 0
        for line in active_tiles:
            running_total += line.count("#")
        if running_total > max_tiles:
            max_tiles = running_total
    for i in range(len(data)):
        active_tiles = []
        clean_data = []
        direction_map = []
        for line in data:
            line = line.strip()
            active_line = ""
            direction_line = []
            for char in line:
                active_line = active_line + "."
                direction_line.append("....")
            clean_data.append(line)
            active_tiles.append(active_line)
            direction_map.append(direction_line)
        direction = "w"
        traceRoute(clean_data, int(i), (len(clean_data[0])-1), direction, active_tiles, direction_map)
        running_total = 0
        for line in active_tiles:
            running_total += line.count("#")
        if running_total > max_tiles:
            max_tiles = running_total
    for i in range(len(data[0])):
        active_tiles = []
        running_total = 0
        clean_data = []
        direction_map = []
        for line in data:
            line = line.strip()
            active_line = ""
            direction_line = []
            for char in line:
                active_line = active_line + "."
                direction_line.append("....")
            clean_data.append(line)
            active_tiles.append(active_line)
            direction_map.append(direction_line)
        direction = "s"
        traceRoute(clean_data, 0, i, direction, active_tiles, direction_map)
        running_total = 0
        for line in active_tiles:
            running_total += line.count("#")
        if running_total > max_tiles:
            max_tiles = running_total
    for i in range(len(data[0])):
        active_tiles = []
        running_total = 0
        clean_data = []
        direction_map = []
        for line in data:
            line = line.strip()
            active_line = ""
            direction_line = []
            for char in line:
                active_line = active_line + "."
                direction_line.append("....")
            clean_data.append(line)
            active_tiles.append(active_line)
            direction_map.append(direction_line)
        direction = "n"
        traceRoute(clean_data, len(clean_data)-1, i, direction, active_tiles, direction_map)
        running_total = 0
        for line in active_tiles:
            running_total += line.count("#")
        if running_total > max_tiles:
            max_tiles = running_total
    print ("Max Energized Tiles: ", max_tiles)





main()
