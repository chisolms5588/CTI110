#Shamara Chisolm
#P5LAB
#05/08/24
#Use random float value.


import random

def disperse_change(amount):
    
    # Calculate dollars, quarters, dimes, nickels, and pennies
    dollars = amount // 100
    quarters = amount % 100 // 25
    dimes = amount % 100 % 25 // 10
    nickels = amount % 100 % 25 % 10 // 5
    pennies = amount % 100 % 25 % 10 % 5 // 1

    # Display the amount of change
    print("Dollars:", int(dollars))
    print("Quarters:", int(quarters))
    print("Dimes:", int(dimes))
    print("Nickels:", int(nickels))
    print("Pennies:", int(pennies))

def main():
    # Generate a random float value as the amount owed
    amount_owed = round(random.uniform(1.0, 100.0), 2)
    print("Amount owed: $" + str(amount_owed))

    #print("Amount owed:", amount_owed)

    # Prompt the user to enter the amount of cash they will put into the self-checkout machine
    amount_paid = float(input("Enter the amount of cash you will put into the self-checkout machine: "))

    # Calculate the amount of change owed to the customer
    change = int(round(amount_paid - amount_owed, 2) * 100)
    print("Change owed: $" + str(change/100))


    # Convert change to an integer and disperse the change
    change_int = round(change * 100)
    disperse_change(change)

if __name__ == "__main__":
    main()
