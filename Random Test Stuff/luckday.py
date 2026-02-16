import random
import numpy
import math
from datetime import datetime

newarray = []
for x in range(0,100):
    newarray.append(random.randint(1,100))
newarray = numpy.array(newarray)

mean_array = math.floor(newarray.mean())

print(f"Today is {datetime.now().date()}. Your random number is {mean_array}.")