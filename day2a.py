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
        trialGood = True
        for i in range(len(trials)):
            if trials[i].isdigit():
                continue
            elif 'blue' in trials[i]:
                if int(trials[i-1]) >14:
                    trialGood = False
            elif 'red' in trials[i]:
                if int(trials[i-1]) >12:
                    trialGood = False
            elif 'green' in trials[i]:
                if int(trials[i-1]) >13:
                    trialGood = False
        if trialGood:
            game = game.split()
            running_total+=int(game[1])
    print(running_total)



main()