#Advent of Code 2023
#Day 11
#Jason R Evarts
import itertools
def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def main():
    file = 'day11data.txt'
    data = importData(file)
    clean_data = []
    expanded_data = []
    new_row = ""
    galaxy_counter = 0
    galaxy_loc_dict = {}
    running_total = 0
    for line in data:
        line = line.strip()
        clean_data.append(line)
    expand_rows = []
    expand_columns = [int(i) for i in range(len(clean_data[0]))]

    #search for rows to expand
    counter = 0
    for line in clean_data:
        #search for rows to expand
        if line.count("#") == 0:
            expand_rows.append(counter)
        #eliminate columns not to expand
        else:
            test_columns = expand_columns.copy()
            for i in test_columns:
                if line[i] == "#":
                    expand_columns.remove(i)
        counter += 1
    #When expand columns is used, we want to start on the right to insert in the correct locations
    expand_columns.sort(reverse=True)
    #When expand rows is used, we want to insert from the bottom up to insert in the correct locations
    expand_rows.sort(reverse=True)
    #expand the columns
    for line in clean_data:
        for i in expand_columns:
            line = line[:i]+"."+line[i:]
        expanded_data.append(line)
    for i in range(len(expanded_data[0])):
        new_row += "."
    for i in expand_rows:
        expanded_data.insert( i , new_row )

    row = 0
    for line in expanded_data:
        column = 0
        if "#" in line:
            for char in line:
                if char == "#":
                    galaxy_counter += 1
                    galaxy_loc_dict[galaxy_counter] = [row, column]
                column += 1
        row += 1
    galaxy_pairs = itertools.combinations(galaxy_loc_dict, 2)
    for item in galaxy_pairs:
        galaxy_1_loc = galaxy_loc_dict[item[0]]
        galaxy_2_loc = galaxy_loc_dict[item[1]]
        dist = abs(galaxy_2_loc[0]-galaxy_1_loc[0])+abs(galaxy_2_loc[1]-galaxy_1_loc[1])
        running_total += dist
    print ("sum of distances between all galaxies: ", running_total)



main()



