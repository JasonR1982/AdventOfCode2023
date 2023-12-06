#Advent of Code 2023
#Day 4
#Jason R Evarts

def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def collectScratch(data, currentCard):
    game = data[currentCard-1] #get current card to evaluate
    max_card = len(data)
    clean_game = game.split(":") #clean off the card #
    winning_numbers, numbers = clean_game[1].split("|") #split the winning numbers from My numbers
    winning_numbers = winning_numbers.split() #Turn string into a list
    numbers = numbers.split() #Turn string into a list
    card_count = 1 #we should count this current card as a collected scratch card
    for num in numbers:
        if num in winning_numbers:
            currentCard += 1
            if currentCard <= max_card:
                card_count += collectScratch(data, currentCard)
    return (card_count)

def main():
    file = "day4data.txt"
    data = importData(file)
    running_total = 0

    for game in data:
        clean_game = game.split(":")
        winning_numbers,numbers = clean_game[1].split("|")
        winning_numbers = winning_numbers.split()
        numbers = numbers.split()
        counter = -1
        for num in numbers:
            if num in winning_numbers:
                counter+=1
        if counter > -1:
            running_total+= 2**counter
    print("Points for part A: ",running_total)

    #part B Option 1
    card_count = 0
    game_count= 1
    for game in data:
        card_count += collectScratch(data, game_count)
        print ("intermediate card count: ", card_count,"\nGame Count: ",game_count)
        game_count +=1
    print ("Card_Count: ", card_count)




main()