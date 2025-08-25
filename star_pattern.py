n=int(input("enter no. of stars: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()



n=int(input("enter no. of stars: "))

for i in range(0, n):
    for j in range(i, n):
        print("*", end=" ")
    print()