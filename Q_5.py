# 5. Write a python program to print a triangular pattern of the alphabet (user input the number 
#    of rows).
#    Example: Input the number of rows = 5, then the pattern should come out as given below.
#    If the count of the alphabet gets exhausted, repeat the alphabet from A.
#    A
#    BC
#    DEF
#    GHIJ
#    KLMNO
#    PQRSTU

rows = int(input("Enter the number of rows\n"))
if rows==0:
    quit()
else:
    pass

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"*((int((rows*(rows+1))/2)))

i = 0
j = 1

while (j<=rows):
    print(letters[i:int(((j*j) + j)/2)])
    i = int(((j*j) + j)/2)
    j = j + 1