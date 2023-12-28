#Advent of Code 2023
#Day 13
#Jason R Evarts
import itertools
def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def findMirrorLine(data):
    line_count = 0
    mirror_line_found = False
    while mirror_line_found == False:
        for line in data:
            if line_count > 0:
                if line == data[line_count-1]:
                    offset = 1
                    while True:
                        if line_count+offset < (len(data)-1) and line_count-offset-1 > 0:
                            if data[line_count + offset] == data[line_count - offset -1]:
                                offset += 1
                            else:
                                break
                        elif line_count+offset == (len(data)-1) or line_count-offset-1 == 0:
                            if data[line_count + offset] == data[line_count - offset - 1]:
                                mirror_line_found = True
                                break
                            else:
                                break
                        else:
                            mirror_line_found = True
                            break
                    if mirror_line_found:
                        break
                    elif line_count > len(data):
                        break
            line_count += 1
        if line_count == len(data):
            break
    if not mirror_line_found:
        return -1
    else:
        return line_count


def main():
    file = ('day13data.txt')
    data = importData(file)
    blocks = []
    new_block = []
    counter = 0
    horizontal_mirror = False
    vertical_mirror = False
    running_total = 0
    for line in data:
        line.strip(" ")
        #write block to list of blocks
        if line == "\n":
            print(new_block)
            blocks.append(new_block)
            counter += 1
            new_block = []
        #create list of strings for each block
        else:
            line = line.strip()
            new_block.append(line)
    #write the last block created to the list of blocks
    blocks.append(new_block)

    horizontal_total = 0
    vertical_total = 0
    line_count = 0
    #analyze each block for a horizontal line of symmetry
    for i in range(len(blocks)):
        vertical_block = []
        # analyze each block for a horizontal line of symmetry
        line_count = 0
        for line in blocks[i]:
            vert_count = 0
            for char in line:
                if line_count == 0:
                    vertical_block.append(char)
                else:
                    vertical_block[vert_count] = vertical_block[vert_count] + char
                    vert_count += 1
            line_count += 1
        vertical_total = findMirrorLine(vertical_block)
        if vertical_total < 0:
            print("Block: ", i, "\nNot Vertical")
            vertical_total = 0
        else:
            vertical_mirror = True
            print("Block: ", i, "\nVertical Total: ", vertical_total)
        horizontal_total = findMirrorLine(blocks[i]) * 100
        if horizontal_total < 0:
            print("Block: ",i,"\nError during horizontal Test")
            horizontal_total = 0
        else:
            horizontal_mirror = True
            print ("Block: ",i,"\nHorizontal Total: ", horizontal_total)


        if vertical_mirror or horizontal_mirror:
            running_total = running_total + vertical_total + horizontal_total
            vertical_mirror = False
            horizontal_mirror = False
            vertical_total = 0
            horizontal_total = 0
            print ("running total: ",running_total)


#data1 = ['#...##..#','#....#..#','..##..###','#####.##.','#####.##.','..##..###','#....#..#']
#print(findMirrorLine(data1))

main()
