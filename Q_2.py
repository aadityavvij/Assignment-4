# 2. Python Program to Print all Numbers in a Range Divisible by a Given Number. (user inputs 
#    the range and the number)

print("Enter Range")

start = int(input("from "))
end = int(input("to "))
list1 = []

gn = int(input("Enter the number with which you want to check the divisibility\n"))

for i in range(start, end+1):
    if (i % gn == 0):
        list1.append(i)
    else:
        continue

print("Numbers in the Range Divisible by the Given Number is/are\n",list1)