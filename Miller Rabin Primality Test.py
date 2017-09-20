import random
import time


def factorise(i):
    k = 0
    while (i - 1) % (2 ** k) == 0:
        k += 1
        if (i - 1) % (2 ** k) != 0:
            k -= 1
            break
    m = int((i - 1) / (2 ** k))
    return m


def isprime(i, a, m):
    b0 = (a ** m) % i
    if b0 == (i - 1) or b0 == 1:
        listX.append(i)
    else:
        return b0


def isprime2(bi, i, count):
    while bi != (i - 1) or bi != 1:
        bi = (b0 ** 2) % i
        if bi == 1:
            pass
        if bi == (i - 1):
            listX.append(i)
        count += 1
        if count == 10:
            break

x = int(input("What limit would you like to inspect:"))
start = time.time()
listX = [2]
for i in range(3, x):
    count = 0
    m = 0
    b0 = 0
    factor = factorise(i)
    a = random.randint(2, (i-1))
    bi = isprime(i, a, factor)
    isprime2(b0, i, count)
end = time.time()
print(len(listX))
print(end - start, "seconds")





