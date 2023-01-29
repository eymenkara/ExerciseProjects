

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def clear():  # Prints 50 blank lines
    print("\n" * 50)

def convert_bid(dolars): # to remove '$' sign and turn to integer
    number = ""
    for i in range(1,len(dolars)):
        number += dolars[i]
    number = int(number)
    return number

max_bid = 0
winner = ""
bids = {}

bidding = True
while bidding:
    #Intro
    print(logo)
    print("Welcome to the secret auction program.")
    #Inputs
    name = input("What is your name? ")
    bid = input("What is your bid? ") #must put dolar sign eg: '$200'
    bid_val = convert_bid(bid)
    #Dict entry
    bids[name] = bid
    #Check max bid
    if max_bid < bid_val:
        max_bid = bid_val
        winner = name
    #Check if bidding complete
    complete = input("Are there any other bidders? Type 'yes' or 'no'.")
    if complete == "no":
        bidding = False
        print(f"The winner is {winner} with a bid of {bids[winner]}.")
    else:
        clear()
