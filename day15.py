#Advent of Code 2023
#Day 15
#Jason R Evarts
import itertools
def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def main():
    file = "day15data.txt"
    data = importData(file)
    clean_data = []
    hash_data = []
    hash_values = []
    boxes = []
    running_total = 0
    for line in data:
        line = line.strip()
        clean_data.append(line)
    for line in clean_data:
        hash_data.extend(line.split(","))
    for i in range(256):
        boxes.append([[],[]])
    for element in hash_data:
        current_value = 0
        lens_id = ''
        char_count = 0
        for char in element:
            if char == "=":
                if lens_id in boxes[current_value][0]:
                    location = boxes[current_value][0].index(lens_id)
                    boxes[current_value][1][location] = element[char_count+1:]
                else:
                    boxes[current_value][0].append(lens_id)
                    boxes[current_value][1].append(element[char_count+1:])
                break
            elif char == "-":
                if lens_id in boxes[current_value][0]:
                    location = boxes[current_value][0].index(lens_id)
                    boxes[current_value][1].pop(location)
                    boxes[current_value][0].pop(location)
                break
            else:
                lens_id = lens_id + char
            current_value += ord(char) #hash step 1 - increase by ascii value
            current_value = current_value * 17 #hash step 2 - multiply by 17
            current_value = current_value%256 #hash step 3 - remainder of value divided by 256
            char_count += 1
    print (boxes)
    box_num = 1
    for box in boxes:
        for j in range(len(box[0])):
            focusing_power = (box_num)*(j+1)*(int(box[1][j]))
            running_total += focusing_power
            print ("Box: ", box_num, "\nFocusing Power: ",focusing_power)
            focusing_power = 0
        box_num += 1
    print ("Total of focusing power: ", running_total)




main()
