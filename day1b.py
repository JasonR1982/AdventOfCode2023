#AdeventOfCode2023
#Day 1
#Jason R Evarts
import re

file1 = open('day1data.txt', 'r')
count = 0
storage = []

while True:
    count += 1
    res = []

    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    replacements = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                    'eight': '8', 'nine': '9'}
    pattern = '|'.join(replacements.keys())
    count=0
    for i in line:
        count+=1
        if i.isdigit():
            first_digit=i
            break
        test1 = line[0:count]
        line2 = re.sub(pattern, lambda match: replacements[match.group(0)], test1)
        first_digit = [int(i) for i in line2 if i.isdigit()]
        if len(first_digit):
            break

    for i in range(len(line)-1,-1,-1):
        if line[i].isdigit():
            second_digit=line[i]
            break
        test2 = line[i:]
        line2 = re.sub(pattern, lambda match: replacements[match.group(0)], test2)
        second_digit = [int(i) for i in line2 if i.isdigit()]
        if len(second_digit):
            break
    numeral = str(first_digit[0]) + str(second_digit[0])
    storage.append(numeral)
    print("Line{}: {}".format(count, line.strip()),"output: ",numeral)

file1.close()
running_total = 0
for i in storage:
    running_total += int(i)

print(running_total)