import math
phii = input('Please enter  geographical latitude (phii) : \n')
phii = int(phii)
landa = input('Please enter  geographical longitude (landa) : \n')
landa = int(landa)
landa0 = input('Please enter  centeral geographical longitude (landa0) : \n')
landa0 = int(landa0)
x = landa - landa0
y = 1/2 * math.log((1 + math.sin(phii)) / (1 - math.sin(phii)))

print('x = ' + str(x) + '\ny = ' + str(y))
