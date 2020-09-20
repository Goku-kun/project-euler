result = []
def checkPrime(x):
  for x in range(2,x):
    if 600851475143%x==0:
      return False
  return True
for x in range(2, 600851475143):
  if(checkPrime(x)):
    if 600851475143%x == 0:
      result.append(x)

print(result)