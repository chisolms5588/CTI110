#Shamara Chisolm
#04/24/24
#P2LAB2
#Write a code that uses a dictionary




# Create the dictionary
car_dict = {
    "Camaro": 22,
    "Prius": 58,
    "Model S": 121,
    "Silverado": 17
}

# Print all the keys in the dictionary
print(*car_dict.keys(), sep=", ")

# Prompt the user to enter a vehicle
chosen_vehicle = input("Enter a vehicle from the list: ")

# Display the MPG for the chosen vehicle
if chosen_vehicle in car_dict:
    mpg = car_dict[chosen_vehicle]
    print(f"The {chosen_vehicle} gets {mpg} MPG.")

    # Prompt the user to enter the number of miles
    miles = float(input("Enter the number of miles you will drive: "))

    # Calculate gallons of gas needed
    gallons_needed = miles / mpg
    print(f"To drive {miles} miles in {chosen_vehicle}, you will need {gallons_needed:.2f} gallons of gas.")
