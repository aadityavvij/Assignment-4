# 8. Input 10 integer values from the user. Write a python program to find and print the following:
#     a. positive numbers
#     b. negative numbers
#     c. odd numbers
#     d. even numbers
#     e. Number of times each number occurs in the List

list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
dict5 = {}


for i in range(0, 10):
    a = int(input("Enter an integer\n"))
    list0.append(a)

for i in list0:
    if i>0:
        list1.append(i)
    else:
        list2.append(i)

    if (i%2!=0):
        list3.append(i)
    else:
        list4.append(i)

    num = list0.count(i)
    dict5.update({i:num})


print("Positive Numbers", list1)
print("Negative Numbers", list2)
print("Odd Numbers", list3)
print("Even Numbers", list4)
print("Number of times each number occurs in the List", dict5)