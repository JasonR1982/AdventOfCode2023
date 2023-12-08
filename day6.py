#Advent of Code 2023
#Day 6
#Jason R Evarts

def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def dist_traveled(vel, time):
    #time is input in milliseconds
    dist = vel * (time)
    return dist

def main():
    data = importData('day6data.txt')
    times = data[0]
    winning_dist = data[1]
    clean_times = times.split(':')
    clean_times_list = clean_times[1].split()
    clean_winning_dist = winning_dist.split(':')
    clean_winning_dist_list = clean_winning_dist[1].split()
    race_index = 0
    running_total = 1
    for time in clean_times_list:
        ways_to_win = 0
        time = int(time)
        for i in range(time):
            move_time = time - i
            dist = dist_traveled(i, move_time)
            if dist > int(clean_winning_dist_list[race_index]):
                ways_to_win += 1
        race_index += 1
        running_total *= ways_to_win
        print ("running total: ", running_total)

    one_race_time = clean_times[1].replace(" ", "")
    one_race_dist = clean_winning_dist[1].replace(" ", "")

    ways_to_win = 0
    time = int(one_race_time)

    for trial in range(int(one_race_time)):
        move_time = time - trial
        dist = dist_traveled(trial, move_time)
        if dist > int(one_race_dist):
            ways_to_win += 1
    print("ways to win one race: ", ways_to_win)




main()
