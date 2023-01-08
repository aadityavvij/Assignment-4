# 6. Write a python program to print the prime numbers for a user input range.

print("Enter the range")
start = int(input("from: "))
end = int(input("to: "))

set0 = set()
set1 = set()

for i in range(start, end+1):
    set0.add(i)
    j = 2
    while j<i:
        if(i%j==0):
            set1.add(i)
            break
        else:
            j = j+1

print(set0-set1)