import numpy
import random

numarray = numpy.array([120, 135, 150, 98, 175, 200, 143]).astype(float)
print(f"Mean: {numarray.mean()}")
print(f"Sum: {numarray.sum()}")
print(f"Max: {numarray.max()}")
print(f"Min: {numarray.min()}")
numarray *= 1.1
print(numarray)

newarray = []
for x in range(0,100):
    newarray.append(random.randint(1,100))
newarray = numpy.array(newarray)

print(f"Mean: {newarray.mean()}")
print(f"Standard Deviation: {newarray.std()}")