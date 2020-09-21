def isPrime(num):
  for i in range(2,num):
    if num%i == 0:
      return False
  return True
j = 2
k = 0
while True:
  if isPrime(j):
    k = k+1
  if k == 10001:
    break
  j = j+1
print(j)