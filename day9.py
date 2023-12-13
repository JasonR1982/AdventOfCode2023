#Advent of Code 2023
#Day 9
#Jason R Evarts

def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def seqDiff(data):
    new_data = []
    for i in range(len(data)-1):
        new_data.append(data[i+1] - data[i])
    if new_data.count(0) == len(new_data):
        new_data.append(0)
        return [i for i in new_data]
    else:
        next_data = []
        next_data.extend(seqDiff(new_data))
        new_data.append(new_data[-1]+next_data[-1])
        return [i for i in new_data]

def revSeqDiff(data):
    new_data = []
    for i in range(len(data) - 1):
        new_data.append(data[i + 1] - data[i])
    if new_data.count(0) == len(new_data):
        new_data.append(0)
        return [i for i in new_data]
    else:
        next_data = []
        next_data.extend(revSeqDiff(new_data))
        new_data.insert(0, new_data[0] - next_data[0])
        return [i for i in new_data]

def main():
    file = "day9data.txt"
    data = importData(file)
    data = [line.strip() for line in data]
    running_total = 0
    for line in data:
        line = line.split()
        line = [int(i) for i in line]
        new_seq = seqDiff(line)
        line.append(line[-1]+new_seq[-1])
        running_total += line[-1]
    print ("Total Seq Forecast: ", running_total)

    rev_total = 0
    for line in data:
        line = line.split()
        line = [int(i) for i in line]
        new_seq = revSeqDiff(line)
        line.insert(0, line[0] - new_seq[0])
        rev_total += line[0]
    print ("Total Rev Forecast: ", rev_total)

main()