# 9. Write a program to count the number of occurrences of each word in the list(List entered 
#    by the user).

list1  = []
dict1 = {}

i = 1

while i==1:
    a = input("Enter a word\n")
    list1.append(a)
    i = int(input("To add a new word, enter 1\nTo move forward, enter 0\n"))

for i in list1:
    c = list1.count(i)
    dict1.update({i : c})

print(dict1)


    