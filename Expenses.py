total = 0 
number_of_expenses = 0
expenses = []

number_of_expenses = int(input("\nHow many expenses do you have?\n\n"))

for i in range(number_of_expenses):
    expense_value = int(input("\nEnter the expense: "))
    expenses.append(expense_value)

total = sum(expenses)
print("\nYour total expenses are $", total,"\n", sep='')
