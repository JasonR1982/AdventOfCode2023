#Advent of Code 2023
#Day 10
#Jason R Evarts

def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def findPath(map, row, column):
    current_pipe = map[row][column]
    map[row] = map[row][:column] + "*" + map[row][column+1:]
    if current_pipe == "*":
        for line in map:
            print (line)
        return
    elif current_pipe == "|":
        if map[row-1][column] == "*":
            findPath(map, row+1, column)
        else:
            findPath(map, row-1, column)
    elif current_pipe == "-":
        if map[row][column-1] == "*":
            findPath(map, row, column+1)
        else:
            findPath(map, row, column-1)
    elif current_pipe == "L":
        if map[row][column+1] == "*":
            findPath(map, row-1, column)
        else:
            findPath(map, row, column+1)
    elif current_pipe == "J":
        if map[row][column-1] == "*":
            findPath(map, row-1, column)
        else:
            findPath(map, row, column-1)
    elif current_pipe == "7":
        if map[row][column-1] == "*":
            findPath(map, row+1, column)
        else:
            findPath(map, row, column-1)
    elif current_pipe == "F":
        if map[row][column+1] == "*":
            findPath(map, row+1, column)
        else:
            findPath(map, row, column+1)
    else:
        print("There is not a pipe adjoining correctly or logic is wrong")
    return

def main():
    file = "day10data.txt"
    data = importData(file)
    map = []
    step_count = 0
    second_step_row = None
    second_step_column = None
    for line in data:
        clean_line = line.strip()
        map.append(clean_line)

    row = 0
    column = 0
    for i in map:
        if "S" in i:
            start_row = row
            for j in i:
                if j == "S":
                    start_column = column
                    map[row] = i[:column] +"*"+ i[column+1:] #turn start symbol into countable marker
                    break
                else:
                    column += 1
            break
        else:
            row += 1
    print ("Start Row: ", start_row, "\n Start Column: ", start_column, "\n", map)
    check_above = True
    check_below = True
    check_left = True
    check_right = True
    if start_row == 0:
        check_above = False
    if start_row == len(map):
        check_below = False
    if start_column == 0:
        check_left = False
    if start_column == len(map[0]):
        check_right = False

    if check_above:
        if map[start_row-1][start_column] == "|" or map[start_row-1][start_column] == "7" or map[start_row-1][start_column] == "F":
            second_step_row = start_row-1
            second_step_column = column
            check_left = False
            check_right = False
            check_below = False
    if check_right:
        if map[start_row][start_column+1] == "-" or map[start_row][start_column+1] == "J" or map[start_row][start_column+1] == "7":
            second_step_row = start_row
            second_step_column = start_column+1
            check_left = False
            check_below = False
    if check_left:
        if map[start_row][start_column-1] == "-" or map[start_row][start_column-1] == "L" or map[start_row][start_column-1] == "F":
            second_step_row = start_row
            second_step_column = start_column-1
            check_below = False
    if check_below:
        if map[start_row+1][start_column] == "|" or map[start_row+1][start_column] == "L" or map[start_row+1][start_column] == "J":
            second_step_row = start_row+1
            second_step_column = start_column

    next_row = second_step_row
    next_column = second_step_column
    while True:
        current_pipe = map[next_row][next_column]
        map[next_row] = map[next_row][:next_column] + "*" + map[next_row][next_column + 1:]
        if current_pipe == "*":
            break
        elif current_pipe == "|":
            if map[next_row - 1][next_column] == "*":
                next_row = next_row + 1
            else:
                next_row =  next_row - 1
        elif current_pipe == "-":
            if map[next_row][next_column - 1] == "*":
                next_column =  next_column + 1
            else:
                next_column =  next_column - 1
        elif current_pipe == "L":
            if map[next_row][next_column + 1] == "*":
                next_row = next_row - 1
            else:
                next_column = next_column + 1
        elif current_pipe == "J":
            if map[next_row][next_column - 1] == "*":
                next_row = next_row - 1
            else:
                next_column =  next_column - 1
        elif current_pipe == "7":
            if map[next_row][next_column - 1] == "*":
                next_row = next_row + 1
            else:
                next_column = next_column - 1
        elif current_pipe == "F":
            if map[next_row][next_column + 1] == "*":
                next_row += 1
            else:
                next_column += 1
        else:
            print("There is not a pipe adjoining correctly or logic is wrong")

    for line in map:
        line_step_count = line.count("*")
        step_count += line_step_count
        print(line)
    halfway = step_count/2
    print ("Step Count: ", step_count, "\n Halfway Steps: ", halfway)



main()

