from art import logo

print(logo)

print("Welcome to the secret auction ")

end_of_program = "yes"

bid_dict = {}

while end_of_program != "no":

    name_bidder = input("What is your name? ")
    bid_price = int(input("What is your bid? (in rupees):"))
    end_of_program = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    bid_dict[name_bidder] = bid_price
    if end_of_program == "no":
        print("Thanks for use secret auction")
    elif end_of_program == "yes":
        print("\n" * 40)
     
bid_name = ""
maxi = 0
for key in bid_dict:
    bidder = bid_dict[key]

    if bidder > maxi:
        maxi = bidder
        bid_name = key

print(f"{bid_name} wrote {bid_dict[bid_name]} bid")
