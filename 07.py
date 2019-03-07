import random
import math
u = random.random()
v = random.random()
z = math.sin (2 * math.pi * v) * math.sqrt (-2 * math.log(u))
print(str(z))