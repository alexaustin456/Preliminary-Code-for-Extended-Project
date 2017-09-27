import random 




def fermat_prime_test():
  
	prime = True
  
	a = random.randint(2, i)
  
	if (a ** (i - 1)) % i == 1:
    
		return prime




def is_composite():
  
	prime = False
  
	a = random.randint(2, i)
  
	m = (a ** (i - 1)) % i
  
	if m != 1:
    
		return prime
  



x = int(input("what limit for primes:"))

listX = [2]

count = 0

for i in range(3, x):
  
is_prime = fermat_prime_test()
  
if is_prime == True:
    
	listX.append(i)
    
	count += 1
  
composite = is_composite()
  
if i in listX:
    
	if composite == True:
      
		listX.remove(i)
    
	else:
      
		pass

print(listX)

print(count)