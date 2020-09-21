def isPythagoreanTriplet(c,a,b):
  if((a*a + b*b) == (c*c)):
    return True
  return False

for c in range(1,1000):
  for a in range(1,1000):
    for b in range(1,1000):
      if ( isPythagoreanTriplet(c,a,b) and (a+b+c==1000)):
        print(a,b,c)
        break
    if ( isPythagoreanTriplet(c,a,b) and (a+b+c==1000)):
      break
  if ( isPythagoreanTriplet(c,a,b) and (a+b+c==1000)):
    break
print(a,b,c)
print(a+b+c," & the product is",(a*b*c))