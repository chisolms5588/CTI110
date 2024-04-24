#Shamara Chisolm
#P2HW2
#04/24/24
#Create a list to enter and grades and output requested data.


#Ask the user to enter grades for tests, each grade should be requested in a seperate statement.

Module_1 = float(input("Enter grade for Module 1:"))
Module_2 = float(input("Enter grade for Module 2:"))
Module_3 = float(input("Enter grade for Module 3:"))
Module_4 = float(input("Enter grade for Module 4:"))
Module_5 = float(input("Enter grade for Module 5:"))
Module_6 = float(input("Enter grade for Module 6:"))

#The program should store the grades entered in a list. Give list a descriptive name.

mod_grades = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]
print()
print("------------Results------------")

#Display the following:

#Lowest grade in list

lowest_grade = min(mod_grades)
print(f"Lowest Grade:  {min(mod_grades)}")

#Highest grade in list

highest_grade= max(mod_grades)
print(f"Highest Grade: {max(mod_grades)}")

#Sum of grades

sum_of_grades = sum(mod_grades)
print(f"Sum of Grades: {sum(mod_grades)}")


#Average of grades

print(f"Average:       {sum_of_grades / len(mod_grades) :.2f}")
print("---------------------------------------")
