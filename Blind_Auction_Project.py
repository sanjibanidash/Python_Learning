import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = " "
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    Name = input("What is your name?\n")
    Price = int(input("How much you want to bid?\n$"))
    bids[Name] = Price
    should_continue = input("Are there any other bidders?\n Type 'Yes' or 'No'. \n").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "Yes":
        print("\n" * 20 )








