i=1
while True:
  k=0
  for j in range(1,21):
    if i%j == 0:
      k = k+1
  if k == 20:
    break
  i = i+1
print(i)