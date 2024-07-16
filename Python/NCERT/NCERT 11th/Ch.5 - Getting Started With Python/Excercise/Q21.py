#Q21
l=int(input('Enter the length of the ladder: '))
Ang=int(input('Enter the value of angle in degrees: '))

import math

ang=Ang*3.14/180
h=l*(math.sin(ang))

print(h) 
