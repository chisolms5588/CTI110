#Shamara Chisolm
#05/04/2024
#P4HW1
#Collect scores using loop instead of an individual statement.


# Ask user to enter for number of scores they would like to enter
num_scores = int(input("How many scores do you want to enter?: "))

# Initialize an empty list to store the scores
test_scores = []

# Loop to collect the scores
for t in range(1, num_scores + 1):
    while True:
        score = int(input(f"Enter Score {t}: "))
        if 0 <= score <= 100:
            test_scores.append(score)
            break
        else:
            print("Invalid score! Please enter a score between 0 and 100.")

# Display the collected scores
print("\n------------Results------------")
print("Scores entered:", test_scores)

#Display the lowest score entered
lowest_score = min(test_scores)
print("Lowest score entered:", lowest_score)

# Create a modified list without the lowest score
modified_scores = test_scores.copy()
modified_scores.remove(lowest_score)

# Calculate the average of scores in the modified list
average_score = sum(modified_scores) / len(modified_scores)
print("Score List after dropping lowest score:", modified_scores)
print("Average score:", average_score)

# Determine the letter grade for the calculated average
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display the letter grade to the user
print("Letter grade:", letter_grade)
