# Python Code to estimate value using Leibniz’s formula
# Import math Library
import math
# Initialize denominator
k = 1
# Initialize sum
s = 0
for i in range(1000000):
    # even index elements are positive
    if i % 2 == 0:
        s += 4/k
    else:
        # odd index elements are negative
        s -= 4/k
    # denominator is odd
    k += 2

print('Value of estimated pi: ' , s)

# Print the value of pi
print('Value of pi from math module: ',math.pi)
