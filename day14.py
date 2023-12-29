#Advent of Code 2023
#Day 14
#Jason R Evarts
import itertools
def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def main():
    file = "day14data.txt"
    data = importData(file)
    clean_data = []
    for line in data:
        line = line.strip()
        clean_data.append(line)
    line_count = 0
    for line in clean_data:
        if line_count > 0:
            char_count = 0  #keep track of character position
            for char in line: #go through each character in the line
                if char == "O": #find rocks to move
                    for i in range(line_count-1,-1,-1):
                        if clean_data[i][char_count] == ".": #check for clear space to the north of the moving rock
                            clean_data[i] = clean_data[i][:char_count] + "O" + clean_data[i][char_count+1:] #move the rock
                            clean_data[i+1] = clean_data[i+1][:char_count] + "." + clean_data[i+1][char_count+1:] #clear the former rock location
                        else:
                            break
                char_count += 1
        line_count += 1
    max_line = len(clean_data) #number of rows in the map
    running_total = 0
    for line in clean_data:
        rock_count = line.count("O")  #count number of rocks in the row
        row_total = rock_count * max_line  #multiply rocks by row number
        running_total += row_total  #add weight to running total
        max_line -= 1 #decrement the row value
    print ("Weight Total: ", running_total)
main()
