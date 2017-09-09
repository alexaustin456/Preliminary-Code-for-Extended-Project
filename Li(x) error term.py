# Error term for Li(x), in this case subtracted off Li(x) as all limits will be less than 10^10^10^34 which is the
# point at Pi(x) and Li(x) cross. From this point onwards Pi(x) is greater than Li(x) but until then it is always
# less than Li(x)
import math
import time
import sys
x = int(input("What limit would you like to select?"))
inf = int(input("What limit for infinity would you like to select?"))
while inf > 10:
    inf = int(input("Sorry the limit for infinity must be less than or equal to 9 for best results, please re-enter"))
i = 0
liX = 0
while i <= inf:
    liX += (math.factorial(i) * x) / ((math.log(x)) ** (i + 1))
    if i == inf:
        print(liX)
        print ((math.sqrt(x) * math.log(x)) / (8 * math.pi))
        print ((liX)-((math.sqrt(x)*math.log(x))/(8*math.pi)))
        print ((math.sqrt(x)*math.log(x))/(8*math.pi))
        time.sleep(2)
        sys.exit()
    else:
        i += 1




