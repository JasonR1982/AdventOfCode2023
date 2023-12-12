#Advent of Code 2023
#Day
#Jason R Evarts

def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def findMapping(input, map):
    found = False
    for mapping in map:
        if input >= mapping[1] and input < (mapping[1] + mapping[2]):
            output = mapping[0] + (input - mapping[1])
            found = True
    if found == False:
        output = input
    return output

def main():
    file = ("day5testdata.txt")
    data = importData(file)
    seeds = data[0]
    seeds = seeds.split(": ")
    seeds = seeds[1].split()
    seeds = [int(i) for i in seeds]
    seed_ranged = []
    for i in range(0,len(seeds),2):
        for j in range(seeds[i],(seeds[i]+seeds[i+1])):
            seed_ranged.append(j)
    #print ("seeds: ", seed_ranged)
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temp = []
    temp_to_humid = []
    humid_to_loc = []
    current_map = []
    possible_planting = []
    for line in data[2:]:
        if "seed-to-soil map:" in line:
            current_map = seed_to_soil
        elif "soil-to-fertilizer" in line:
            current_map = soil_to_fertilizer
        elif "fertilizer-to-water" in line:
            current_map = fertilizer_to_water
        elif "water-to-light" in line:
            current_map = water_to_light
        elif "light-to-temperature" in line:
            current_map = light_to_temp
        elif "temperature-to-humidity" in line:
            current_map = temp_to_humid
        elif "humidity-to-location" in line:
            current_map = humid_to_loc
        elif line == "\n":
            continue
        else:
            line = line.strip()
            line = line.split()
            line = [int(i) for i in line]
            current_map.append(line)

    for seed in seed_ranged:
        soil = findMapping(seed, seed_to_soil)
        #print ("soil: ",soil)
        fertilizer = findMapping(soil, soil_to_fertilizer)
        #print ("fertilizer: ", fertilizer)
        water = findMapping(fertilizer, fertilizer_to_water)
        #print ("water: ", water)
        light = findMapping(water, water_to_light)
        #print ("light: ", light)
        temp = findMapping(light, light_to_temp)
        #print ("temp: ", temp)
        humid = findMapping(temp, temp_to_humid)
        #print ("humid: ", humid)
        location = findMapping(humid, humid_to_loc)
        #print ("location: ", location)
        possible_planting.append(location)
    possible_planting.sort()
    print (possible_planting[0])





main()