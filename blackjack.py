import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""



deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#Draws one random card
def pull_card(deck_list):
    card = random.choice(deck_list)
    return card

#Calculates and displays hand, also modifies Ace if sum exceeds 21
def display(hand, name):
    total = 0
    for card in hand:
        total += card
    if total > 21:
        for i in range(0, len(hand)):
            if hand[i] == 11:
                hand[i] = 1
        total = 0
        for card in hand:
            total += card

    print(f"{name}: {hand}    ({total})")






#Game code
end = False
while not end:
    print(logo)
    player_hand = []
    ai_hand = []
    #Player first two cards
    player_hand.append(pull_card(deck))
    player_hand.append(pull_card(deck))
    #AI first card
    ai_hand.append(pull_card(deck))

    busted = False # will be true if anyone is busted

    # Player Draw Card Loop
    keep_drawing = True
    while keep_drawing:
        #Display Hands
        display(ai_hand, "Opponent")
        display(player_hand, "You")
        #Check Busted
        if sum(player_hand) > 21:
            print("Busted!")
            print("You Lost!")
            busted = True
            keep_drawing = False
        else:
            answer = input("Would you like to draw? Type 'draw' or 'stop'. ")
            if answer == "draw":
                player_hand.append(pull_card(deck))
            elif answer == "stop":
                keep_drawing = False
            else:
                print("Wrong input...")

    if not busted:
        ai_hand.append(pull_card(deck))  # AI draws second card

        # AI Draw Card Loop
        ai_draws = True
        while ai_draws:
            display(ai_hand, "Opponent")
            display(player_hand, "You")
            if sum(ai_hand) < 17:                   #AI Draws (total<17)
                ai_hand.append(pull_card(deck))
            else:
                if sum(ai_hand) > 21:               #AI Busted (total>21)
                    print("Opponent Busted!")
                    print("You Win!")
                    busted = True
                    ai_draws = False
                else:                               #AI Stays (16<total<22)
                    ai_draws = False

        # Comparing Hands
        if not busted:
            if sum(player_hand) > sum(ai_hand):
                # Win
                print("You Win!")
            elif sum(player_hand) < sum(ai_hand):
                # Lose
                print("You Lost!")
            else:
                #Tie
                print("Tie!")

    # Play again?
    again = input("Would you like to play again? Type 'yes' or 'no' ")

    if again == "no":
        end = True

