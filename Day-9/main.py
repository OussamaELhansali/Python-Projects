# from replit import clear

from art import logo

# HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program")
bidders = {}
new_bidder = True
while new_bidder:
    name = str(input("What's your name ?\n"))
    bid = int(input("What's your bid? $"))
    bidders[name] = bid
    x = str(input("Is there another bidder in the room? Yes or No."))
    if x.lower() == "no":
        new_bidder = False
        winner = list(bidders.keys())[0]
        for i in bidders.keys():
            if bidders[i] >= bidders[winner]:
                winner = i
            else:
                pass
        print(f"The winner is {winner} with a bid of {bidders[winner]} $ ")
    else:
        pass
