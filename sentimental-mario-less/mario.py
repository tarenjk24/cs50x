# TODO

from cs50 import get_int

while True:
    x = get_int("Enter pyramid height between 1-8: ")
    if x > 0 and x < 9:
       break


for j in range(0,x,1):
    for i in range(0,x,1):
        if (j + i  < x - 1):
            print(" ", end="")
        else:
            print("#", end="")
    print()



