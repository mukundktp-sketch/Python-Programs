n=int(input("enter no. of stars: "))

for i in range(0, n+1):
    for j in range(i+1, n+1):
        print("*", end=" ")
    print()