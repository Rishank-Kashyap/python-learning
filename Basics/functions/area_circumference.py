import math

num = int(input("Enter the radius of the circle: "))


def area_circumference(radius):
    return math.pi * radius * radius, 2 * math.pi * radius


area, circumference = area_circumference(num)

print("Area :", area, ", Circumference :", circumference)
