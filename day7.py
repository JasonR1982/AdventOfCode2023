#Advent of Code 2023
#Day 6
#Jason R Evarts

def importData(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def determine_basic_rank(hand):
    counts = []
    rank = 0
    for i in range(5):
        counts.append(hand.count(hand[i]))
    if 5 in counts:
        rank = 7
    elif 4 in counts:
        rank = 6
    elif 3 in counts:
        if 2 in counts:
            rank = 5
        else:
            rank = 4
    elif 2 in counts:
        if counts.count(2) > 2:
            rank = 3
        else:
            rank = 2
    else:
        rank = 1
    return rank

#takes in two cards and returns:
#   -1 for card1 less than card2
#   0 for equal cards
#   1 for card1 bigger than card2
def compare_card(card1, card2):
    char = card1
    test_char = card2
    if char == test_char:
        return 0
    elif char == "A":
        return 1
    elif char == "K" and test_char == "A":
        return -1
    elif char == "Q" and test_char in ["A","K"]:
        return -1
    elif char == "J" and test_char in ["A","K","Q"]:
        return -1
    elif char == "T" and test_char in ["A","K","Q","J"]:
        return -1
    else:
        # hand for test_char must be ranked higher than current hand, so far
        if test_char.isalpha() and char.isalpha():
            return 1
        if test_char.isalpha(): #hand for test_char must be ranked higher than current hand
            return -1
        # if char is alpha and test char is num the below should trigger to put current
        # hand above test hand
        elif char.isalpha():
            return 1
        elif int(char) > int(test_char):
            return 1
        else:
            return -1

def hand_sorting(hand_list):
    sorted_hand_list = []
    sorted_hand_list.append(hand_list.pop())
    if len(hand_list) > 0:
        for i in range(len(hand_list)):
            current_hand = hand_list.pop(0)
            index = 0
            searching = True
            appended = False
            for i in range(len(sorted_hand_list)):
                for card in sorted_hand_list[i][index]:
                    comparison = compare_card(card, current_hand[0][index])
                    if comparison == 0:
                        index += 1
                        second_compare = compare_card(sorted_hand_list[i][0][index], current_hand[0][index])
                        if second_compare == 1:
                            sorted_hand_list.insert(i, current_hand)
                            appended = True
                            break
                        elif second_compare == 0:
                            index += 1
                            third_compare = compare_card(sorted_hand_list[i][0][index], current_hand[0][index])
                            if third_compare == 1:
                                sorted_hand_list.insert(i, current_hand)
                                appended = True
                                break
                            elif third_compare == 0:
                                index += 1
                                fourth_compare = compare_card(sorted_hand_list[i][0][index], current_hand[0][index])
                                if fourth_compare == 1:
                                    sorted_hand_list.insert(i, current_hand)
                                    appended = True
                                    break
                                elif fourth_compare == 0:
                                    index += 1
                                    fifth_compare = compare_card(sorted_hand_list[i][0][index], current_hand[0][index])
                                    if fifth_compare == 1:
                                        sorted_hand_list.insert(i, current_hand)
                                        appended = True
                                        break
                                    else:
                                        index = 0
                                        break
                                else:
                                    index = 0
                                    break
                            else:
                                index = 0
                                break
                        else:
                            index = 0
                            break
                    elif comparison == 1:
                        sorted_hand_list.insert(i, current_hand)
                        appended = True
                        searching = False
                        break
                    else:
                        break
                if appended:
                    break
            if appended == False:
                sorted_hand_list.append(current_hand)

    return sorted_hand_list




def main():
    file = ("day7data.txt")
    data = importData(file)
    total_winnings = 0
    hands = []
    high_card = []
    one_pair = []
    two_pair = []
    three = []
    full_house = []
    four = []
    five = []
    final_order = []
    index = 0
    for i in data:
        hands.append(i.split()) #hands is list of lists
        index += 1
    for hand in hands:
        basic_rank = int(determine_basic_rank(hand[0]))
        if basic_rank == 7:
            five.append(hand)
        elif basic_rank == 6:
            four.append(hand)
        elif basic_rank == 5:
            full_house.append(hand)
        elif basic_rank == 4:
            three.append(hand)
        elif basic_rank == 3:
            two_pair.append(hand)
        elif basic_rank == 2:
            one_pair.append(hand)
        elif basic_rank == 1:
            high_card.append(hand)
        else:
            print("something terrible happened with basic rank")
    if len(five):
        sorted_five = hand_sorting(five)
        sorted_five.reverse()
        final_order.extend(sorted_five)
    if len(four):
        sorted_four = hand_sorting(four)
        sorted_four.reverse()
        final_order.extend(sorted_four)
    if len(full_house):
        sorted_full = hand_sorting(full_house)
        sorted_full.reverse()
        final_order.extend(sorted_full)
    if len(three):
        sorted_three = hand_sorting(three)
        sorted_three.reverse()
        final_order.extend(sorted_three)
    if len(two_pair):
        sorted_two_pair = hand_sorting(two_pair)
        sorted_two_pair.reverse()
        final_order.extend(sorted_two_pair)
    if len(one_pair):
        sorted_one_pair = hand_sorting(one_pair)
        sorted_one_pair.reverse()
        final_order.extend(sorted_one_pair)
    if len(high_card):
        sorted_high_card = hand_sorting(high_card)
        sorted_high_card.reverse()
        final_order.extend(sorted_high_card)
    num_of_hands = len(final_order)
    remaining_hands = num_of_hands
    for i in final_order:
        print ("Hand : ", i[0], "Hand Number: ", remaining_hands)
        total_winnings += (int(i[1])*remaining_hands)
        remaining_hands -= 1
    print ("Total Winnings: ", total_winnings, "\nTotal Hands: ", len(data), "\nTotal in Final Order: ", num_of_hands)





main()
