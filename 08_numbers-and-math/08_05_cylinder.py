# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

from math import pi

radius = 3.14
height = 5
circumference = 2*pi*radius
area = pi*radius**2
volume = area*height
surface = (2*area)+(circumference*height)

print(volume, surface)