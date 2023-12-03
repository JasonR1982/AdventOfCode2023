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
        return int(left), int(right)
    elif line[columnIndex].isdigit():
        left = searchPartNumber(line,columnIndex,-1)
        right = searchPartNumber(line,columnIndex,1)
        number = left + line[columnIndex] + right
        return int(number), 0
    else:
        number = 0
        return int(number),int(number)




def main():
    file = ("day3data.txt")
    data = importData(file)
    #print(data) #ensure Data has imported
    rowCount=0
    running_total = 0
    for line in data:
        columnCount=0 #counter for keeping track of location along row

        for i in line:
            left = 0
            right = 0
            aboveLeft = 0
            aboveRight = 0
            belowLeft
            belowRight = 0
            if i.isdigit() or i == "." or i =="\n": #keep moving for anything that's not a symbol
                columnCount +=1
                #print(i,end="") #testing for finding special characters
            else: #found a symbol or a letter
                #print("found",end="") #testing for finding special characters
                #search to the left of the symbol
                leftCheck = searchPartNumber(line,columnCount,-1)
                if not leftCheck == "": #if nothing on left, keep left = 0
                    left = int(leftCheck)
                rightCheck = searchPartNumber(line,columnCount,1)
                if not rightCheck == "": #if nothing on right, keep right = 0
                    right = int(rightCheck)
                if rowCount >0: #keep from rolling over the top of the array
                    aboveLeft, aboveRight = searchPartNumberAdjacentLine(data[rowCount-1],columnCount)
                if rowCount < len(data): #keep from checking outside the array
                    belowLeft, belowRight = searchPartNumberAdjacentLine(data[rowCount+1],columnCount)
                gearRatio = []
                if i == "*":
                    if aboveLeft:
                        gearRatio.append(aboveLeft)
                    if aboveRight:
                        gearRatio.append(aboveRight)
                    if belowLeft:
                        gearRatio.append(belowLeft)
                    if belowRight:
                        gearRatio.append(belowRight)
                    if left:
                        gearRatio.append(left)
                    if right:
                        gearRatio.append(right)
                    if len(gearRatio) == 2: #need to check that ONLY two part numbers are adjacent to the symbol
                        running_total+= (gearRatio[0]*gearRatio[1])
                left = 0
                right = 0
                above = 0
                below = 0
                columnCount += 1
        rowCount += 1 #increment counter after processing row
    print (running_total)







main()