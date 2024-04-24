#Shamara Chisolm
#04/12/24
#P1HW2
#This program will calculate and display travel expenses.


#Ask user to enter their budget

budget = float(input("Enter your budget:"))

#Ask user to enter travel destination

destination = input("Enter your travel destination:")

#Ask user for amount they will spend on gas

gas = float(input("Approximately how much will you spend on gas? "))

#Ask user for amount they will spend on accomodation

accomodation = float(input("How much do you plan to spend on a hotel? "))

#Ask user for amount they will spend on food

food = float(input("Finally, how much do you need for food? "))

#Add expenses

expenses = gas + accomodation + food

#Subtract expenses from budget

remaining_balance = budget - expenses

#Display results

print("----------------Travel Expenses-----------------")
print(f"Location:         {destination}")
print(f"Initial Budget:   ${budget :.2f}")
print(f"Fuel:             ${gas :.2f}")
print(f"Accomodation:     ${accomodation :.2f}")
print(f"Food:             ${food :.2f}")
print("-------------------------------------------------")
print()
print(f"Remaining Balance:${remaining_balance :.2f}")
