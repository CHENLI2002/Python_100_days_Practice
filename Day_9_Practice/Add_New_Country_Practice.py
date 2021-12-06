import os
import time

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
print(logo)

print("Welcome to the secrete auction program.")

def find_winner(name_dic):
    highest = 0
    name = ""
    
    for key in name_dic:
        if int(name_dic[key]) > highest:
            name = key
            highest = int(name_dic[key])
    
    os.system('cls')
    print(f"The winner is {name} with a bid of ${highest}.\n")
    time.sleep(3)

def get_bids():
    another_or_not = True
    all_bidder = {}
    
    while another_or_not:
        name = input("What is your name?: ")
        amount = input("What's your bid?: $")
        all_bidder[name] = amount
        another = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        
        if another == 'yes':
            os.system('cls')
        else:
            another_or_not = False
    
    return all_bidder

find_winner(get_bids())
