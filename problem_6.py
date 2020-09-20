def square(num):
  return num*num

sum_of_squares = 0
sum = 0
for i in range(1,101):
  sum_of_squares = sum_of_squares + square(i)
  sum = sum + i

print(abs(square(sum)- sum_of_squares))