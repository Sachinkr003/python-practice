#Circumference of a circle 

import math

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi *  radius

print(f"The circumference is: {circumference}")

#If you need value in decimal then,

print(f"The circumference is: {round(circumference, 2)}")