import numpy as np
fib_list = [1, 2]
var_1 = 1
var_2 = 2
sum=0
while True:
    temp = var_1 + var_2
    if temp >= 4000000:
        break
    fib_list.append(temp)
    var_1 = var_2
    var_2 = temp
for num in fib_list:
    if num%2 == 0:
        print(num, end=" ")
        sum = sum + num
print()
print(sum)