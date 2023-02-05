# Get the loan details
money_owed = float(input("\nHow much money do you owe? \n\n"))
apr = float(input("\nWhat is annual percentage rate?\n\n"))
payment = float(input("\nWhat will the monthly payment be?\n\n"))
months = int(input("\nHow many months do you want to see results for?\n\n"))

# Divide the APR by 100 to make a % then by 12 to make it monthly

monthly_rate = apr/100/12

for i in range(months):
    # Add in the intrest

    intrest_paid = money_owed * monthly_rate
    money_owed = money_owed + intrest_paid

    # Check if we are on the last payment

    if ((money_owed - payment) < 0):
        print("\nThe last payment is", money_owed)
        print("\nYou paid off the loan in", i+1, "months\n")
        break

    # Make payments

    else:
        money_owed = money_owed - payment

        # Print the results after this month

        print("\nPaid", payment, "of which", intrest_paid, "was interest;", end= ' ')
        print("Now I owe", money_owed)