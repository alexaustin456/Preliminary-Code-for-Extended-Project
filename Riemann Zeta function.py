import math
import time
import sys
x = int(input("What limit would you like to select?"))
zeros = open("riemann.txt")
p = []
for non_trivial in zeros:
    p.append(float(non_trivial.strip()))
print(len(p))
print(p)
ser = 0
for i in range (0,99):
    ser += (x**p[i])/(p[i])
print(ser)
piX = -(ser)+x-(0.5*(math.log(1-x**2))-(math.log(2*math.pi)))
print(piX)
