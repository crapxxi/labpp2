import math
n = int(input("Input degree: "))
print("Output radian: " + str(math.radians(n)))

import math
h = int(input("Height: "))
bf = int(input("Base, first value: "))
bs = int(input("Base, second value: "))
print("Expected output: " + str((bf+bs)/2*h))


import math
s = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
print("Input the length of a side: " + str((s*l*(l/(2*math.tan(math.pi/s))))/2))

import math
s = int(input("Length of base: "))
l = int(input("Height of parallelogram: "))
print("Expected Output: " + str(s*l))