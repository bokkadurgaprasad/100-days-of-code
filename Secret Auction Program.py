#Secret Auction Program
import os

bids = {}
bid_finished = False

def highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with bid of ${highest_bid}")


while not bid_finished:
    name = input("what is your name?\n")
    price = int(input("What is bid?\n$"))
    bids[name] = price
    should_continue = input("Are there any bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bid_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')
