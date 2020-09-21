def countdivisors(num):
  count = 0
  for i in range(1, num+1):
    if num % i == 0:
      count = count + 1
  if (count>500):
    return True
  return False

sum=0
i = 1
number = 0
while True:
  sum = sum + i
  if(countdivisors(sum)):
    number = sum
    break
  i = i + 1

print(number)