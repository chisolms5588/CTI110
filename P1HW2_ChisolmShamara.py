#Shamara Chisolm
#04/12/24
#P1HW2
#This program will calculate and display travel expenses.


#Ask user to enter their budget

budget = int(input("Enter your budget:"))

#Ask user to enter travel destination

destination = input("Enter your travel destination:")

#Ask user for amount they will spend on gas

gas = int(input("Approximately how much will you spend on gas? "))

#Ask user for amount they will spend on accomodation

accomodation = int(input("How much do you plan to spend on a hotel? "))

#Ask user for amount they will spend on food

food = int(input("Finally, how much do you need for food? "))

#Add expenses

expenses = gas + accomodation + food

#Subtract expenses from budget

remaining_balance = budget - expenses

#Display results

print("----------------Travel Expenses-----------------")
print("Location: ",destination)
print("Initial Budget: ",budget)
print()
print("Fuel: ",gas)
print("Accomodation: ",accomodation)
print("Food: ",food)
print()
print("Remaining Balance: ",remaining_balance)
