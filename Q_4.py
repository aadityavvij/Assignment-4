# 4. Write a Python program to construct the following pattern, using a nested for loop.
#    *
#    * *
#    * * *
#    * * * *
#    * * * * *
#    * * * *
#    * * *
#    * *
#    *

star = "* "

i = 1
while i<6:
    print(star * i)
    i = i+1

j = 4
while j>0:
    print(star * j)
    j = j-1