# Ask the user to enter employee information
employee_name = input("Enter the name of the employee: ")

#Ask user to enter number of hours worked for the week
hours_worked = float(input("Enter the number of hours the employee worked this week: "))

#Ask use to enter employees pay rate
pay_rate = float(input("Enter the employee's pay rate: "))

# Evaluate if the employee has worked overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate overtime pay
overtime_pay_rate = pay_rate * 1.5
overtime_pay = overtime_hours * overtime_pay_rate

# Calculate pay for regular hours
regular_pay = regular_hours * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

print("------------------------------")
print()

# Display employee information and pay details
print("Employee Name:", employee_name)
print()
print("Hours Worked  Pay Rate  OverTime  Overtime Pay  Regular Pay  Gross Pay")
print("-----------------------------------------------------------------------")
print(f'{hours_worked:<15.2f} {pay_rate:<7.2f} {overtime_pay:<12.2f} {overtime_pay_rate:<12.2f} ${regular_pay:<10.2f} ${gross_pay:<15.2f}')

