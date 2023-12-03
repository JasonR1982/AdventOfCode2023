#Advent of Code 2023
#Day 3
#Jason R Evarts

def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def searchPartNumber(line, columnIndex, direction):
    if columnIndex>-1 and columnIndex<len(line):
        if line[columnIndex+direction].isdigit():
            result = searchPartNumber(line,columnIndex+direction,direction)
            if direction == 1:
                result = line[columnIndex+direction] + result
                return result
            else:
                result += line[columnIndex+direction]
                return result
        else:
            return ""
    else:
        return ""

def searchPartNumberAdjacentLine(line, columnIndex):
    if line[columnIndex] == ".":
        left = searchPartNumber(line,columnIndex,-1)
        right = searchPartNumber(line,columnIndex,1)
        if left == '':
            left = '0'
        if right == '':
            right = '0'
        number = int(left) + int(right)
        return number
    elif line[columnIndex].isdigit():
        left = searchPartNumber(line,columnIndex,-1)
        right = searchPartNumber(line,columnIndex,1)
        number = left + line[columnIndex] + right
        return int(number)
    else:
        number = 0
        return number




def main():
    file = ("day3data.txt")
    data = importData(file)
    print(data)
    rowCount=0
    running_total = 0
    for line in data:
        columnCount=0

        for i in line:
            left = 0
            right = 0
            above = 0
            below = 0
            if i.isdigit() or i == "." or i =="\n":
                columnCount +=1
                #print(i,end="") #testing for finding special characters
            else:
                #print("found",end="") #testing for finding special characters
                #search to the left of the symbol
                leftCheck = searchPartNumber(line,columnCount,-1)
                if not leftCheck == "": #if nothing on left, keep left = 0
                    left = int(leftCheck)
                rightCheck = searchPartNumber(line,columnCount,1)
                if not rightCheck == "": #if nothing on right, keep right = 0
                    right = int(rightCheck)
                if rowCount >0: #keep from rolling over the top of the array
                    above = searchPartNumberAdjacentLine(data[rowCount-1],columnCount)
                if rowCount < len(data): #keep from checking outside the array
                    below = searchPartNumberAdjacentLine(data[rowCount+1],columnCount)
                running_total+= left + right + above + below
                left = 0
                right = 0
                above = 0
                below = 0
                columnCount += 1
        rowCount += 1 #increment counter after processing row
    print (running_total)







main()