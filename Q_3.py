# 3. Program to calculate the area of a triangle using heron’s formula. (check condition 
#    if the combination of sides is possible).
import math

a = int(input("Enter the first side length\n"))
b = int(input("Enter the second side length\n"))
c = int(input("Enter the third side length\n"))

s = (a+b+c)/2

area_square = s*(s-a)*(s-b)*(s-c)

if (area_square > 0):
    print("Area of the triangle is", math.sqrt(area_square))

else:
    print("Triangle not formed!")
