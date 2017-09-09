import math
import time
import sys
x = int(input("What limit would you like to select?"))
inf = int(input("What limit for infinity would you like to select?"))
while inf > 3:
    inf = int(input("Sorry the limit for infinity must be less than or equal to 3 for best results, please re-enter"))
i = 0
liX = 0
while i <= inf:
    liX += (math.factorial(i) * x) / ((math.log(x)) ** (i + 1))
    if i == inf:
        print (liX)
        time.sleep(2)
        sys.exit()
    else:
        i += 1



