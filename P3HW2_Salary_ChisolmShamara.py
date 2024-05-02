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
print(f'\n{"Hours Worked":<12} {"Pay Rate":<12} {"OverTime":<12} {"Overtime Pay":<14} {"Regular Pay":<12} {"Gross Pay":<12}')
print("-----------------------------------------------------------------------------")
print(f'{hours_worked:<12.2f} {pay_rate:<12.2f} {overtime_pay:<12.2f} {overtime_pay_rate:<14.2f} ${regular_pay:<12.2f} ${gross_pay:<12.2f}')
