# Scissor Paper And Rock Game

import random

user_score = 0
comp_score = 0
ties = 0
item_list = ["scissor", "paper", "rock"]

name = input("Enter the name of player: ")
# Removed the incorrect assignment of comp_choice here

def menu():
    global name
    print("****************")
    print(f"Welcome, {name} to Scissor, Paper & Rock Game!")
    print("**************************************")
    print("You have three choices:")
    print("Type scissor, paper, rock (any one):")

def computer():
    # Function to randomly select computer's choice
    return random.choice(item_list)

# In that condition where Users and Computer Choose the Same Element or s, p, r
def winner(user_choice, comp_choice):
    global user_score, comp_score, ties
    if user_choice == comp_choice:
        return "Tie"
    
    elif (user_choice == "scissor" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "rock" and comp_choice == "scissor"):  # Human wins conditions
        user_score += 1
        return "Human Wins."
    else:
        comp_score += 1
        return "Bot Wins."

while True:
    menu()
    user_choice = input("Enter or Type scissor, paper, rock (any one): ").lower()  # Fixed the .lower() call
    
    if user_choice == "exit":
        print("Thanks for playing! My games!")
        print("Your final score looks like this:")
        print(f"You scored {user_score} points, Bot scored {comp_score} points, Ties: {ties} times")
        break
    elif user_choice not in item_list:
        print("Invalid choice, please try again.")
        continue  # This will skip the rest of the loop and ask the player again for a valid choice

    comp_choice = computer()  # Get the computer's choice

    print(f"Bot has chosen: {comp_choice}")

    result = winner(user_choice, comp_choice)
    print(result)

    if result == "Tie":
        ties += 1

    print("Current Scores:")
    print(f"You Score: {user_score} and Bot Score: {comp_score}")
