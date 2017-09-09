import math
def sieve():
    count = 0
    x = int(input("What limit would you like to select?"))
    listX = range(3, x)
    for i in range(2, x):
        a = 2
        while a <= x:
            if i*a in listX:
                listX.remove(i*a)
                count += 1
            a += 1
    print(listX)
    print(x-count-2)#loop starts at 3 rather than zero
sieve()









