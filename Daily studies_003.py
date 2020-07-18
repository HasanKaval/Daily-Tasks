#Write a Python code to get lengths of a triangle from a user and then check them whether this triangle is equilateral, isosceles or scalene.

x = (int(input("Please enter the length of the first side of your triangle")))
y = (int(input("Please enter the length of the second side of your triangle")))
z = (int(input("Please enter the length of the third side of your triangle")))

if x == y == z :
  print("This is an equilateral triangle.")
if x == y or x == z or z == y :
  print("This is an isosceles triangle.")
else :
  print("This is an scalene triangle.")
print()
