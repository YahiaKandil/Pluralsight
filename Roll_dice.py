import random  
roll = random.randint(1,6)

user_input= int(input("Guess the dice number: \n"))

if user_input == roll:
    print("You are correct!")
else:
    print("Wrong! The computer rolled " + str(roll))
