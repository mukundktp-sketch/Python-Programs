n=int(input("enter highest no. of stars: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

for i in range(1,n+1):
    for j in range(1,n+1-i):
        print("*", end=" ")
    print()