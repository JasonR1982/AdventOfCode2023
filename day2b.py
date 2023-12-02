#Advent of Code 2023
#Day 2
#Jason R Evarts

def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def main():
    file = ("day2data.txt")
    data = importData(file)
    running_total = 0
    for entry in data:
        game,trials = entry.split(':')
        trials = trials.split()
        redMin = 0
        blueMin = 0
        greenMin = 0
        for i in range(len(trials)):
            if trials[i].isdigit():
                continue
            elif 'blue' in trials[i]:
                if int(trials[i-1]) > blueMin:
                    blueMin = int(trials[i-1])
            elif 'red' in trials[i]:
                if int(trials[i-1]) > redMin:
                    redMin = int(trials[i-1])
            elif 'green' in trials[i]:
                if int(trials[i-1]) > greenMin:
                    greenMin = int(trials[i-1])
        gamePower = redMin * greenMin * blueMin
        running_total+=gamePower
    print(running_total)



main()