a = int(input("Enter first angle of the triangle: "))
b = int(input("Enter second angle of the triangle: "))
c = int(input("Enter third angle of the triangle: "))

if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    if a < 90 and b < 90 and c < 90:
        print("This is an acute angle triangle")
    elif a == 90 or b == 90 or c == 90:
        print("This is a right angle triangle")
    else:
        print("This is an obtuse angle triangle")
else:
    print("Not a valid triangle")
