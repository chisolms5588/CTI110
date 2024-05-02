#Shamara Chisolm
#P4LAB2
#05/02/24
#Loops output range.


#get the first number assign to variable
num_1 = int(input())

#get the second number assign to variable
num_2 = int(input())

#evaluate if second int is less than the first, if yes dispay the statement

if num1 < num2:
    print("Second integer can't be less than the first.")

#if num1 < num2, then print the first number adn subsequence in increments of 5, stop at second number
elif num_1 <= num_2:
    while num_1 <= num_2:
        print(num_1, end=" ")
        num_1 += 5
    print()  # newline
