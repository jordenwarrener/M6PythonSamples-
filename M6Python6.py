import math
n = int(input('Enter an integer:'))
result = 1
for i in range(1, n+1):
    result = result * i
print('factorial of {} using for loop:{}'.format(n, result))
print('factorial of {} using inbuilt function:{}'.format(n, math.factorial(n)))
