import math

tetha = input ('Please Enter the angle in DEG : ')
tethaForOut = tetha 
tetha = float (tetha)
tetha = (tetha * math.pi) / 180
out = (math.sin(tetha) ** 2) + (math.cos(tetha) ** 2)
print ('Sin^2 (' + str(tethaForOut) + ') + Cos^2 (' + str(tethaForOut) + ') = ' + str(out))

