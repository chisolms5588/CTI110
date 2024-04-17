# Shamara Chisolm
#04/17/24
#P2LAB1
#Variables and Expressions



#Using the radius given by user the program should calculate the diameter, circumference, and area of a circle




#Enter radius

radius = float(input("What is the radius of the circle? "))

#Calculate the diameter of the circle

diameter = 2*radius
print (f"The diameter of the circle is {diameter :.2f}")

#Calculate the circumference of the circle

_pi = 3.14159
cir_cum = 2*_pi*radius
print (f"The circumference of the circle is {cir_cum :.2f}")

#Calculate the area of the circle

area = _pi * radius ** 2
print (f"The area of the circle is {area :.2f}")

