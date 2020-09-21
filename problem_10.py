import numpy as np
def isPrime(num):
  for i in range(2,num):
    if(num%i==0):
      return False
  return True

list_prime = []
for i in range(2000000):
  if (isPrime(i)):
    list_prime.append(i)

print(np.sum(list_prime))