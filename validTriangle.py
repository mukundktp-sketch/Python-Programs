a = int(input("Enter first angle of the triangle: "))
b = int(input("Enter second angle of the triangle: "))
c = int(input("Enter third angle of the triangle: "))

if a + b + c == 180:
    print("valid triangle")
else:
    print("not valid triangle")