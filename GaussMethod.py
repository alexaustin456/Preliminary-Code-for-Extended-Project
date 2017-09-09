#Method of Gauss (x/lnx)
import math
x = int(input("What limit would you like to select?"))
piX = x/(math.log(x))
print "pi(x) =", (piX)
piX = int(round(piX,0))
print "pi(x) =", (piX),"(To the nearest integer)"