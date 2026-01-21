import sys
import math
x = 0
y = 1
z = 1

sys.set_int_max_str_digits(round(math.inf))

print(x)
print(y)
for x in range(50000000):
    print(z)
    x = y
    y = z
    z = x+y