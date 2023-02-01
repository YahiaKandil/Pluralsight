import random

computer_choice = random.choice(["rock", "paper", "scissor"])
user_choice = input("\n\nEnter your choice: \n\n")

if computer_choice == user_choice:
    print("\nIt's a tie! \n")

elif computer_choice == "rock" and user_choice == "paper":
    print("\nYou won!, the computer picked " + computer_choice +"\n")


elif computer_choice == "paper" and user_choice == "scissor":
    print("\nYou won!, the computer picked " + computer_choice +"\n")


elif computer_choice == "scissor" and user_choice == "rock":
    print("\nYou won!, the computer picked " + computer_choice +"\n")

else:
    print("\nYou lost!, the computer picked " + computer_choice +"\n")