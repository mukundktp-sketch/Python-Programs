N=int(input("Enter a number:"))
sum=0
for i in range(1,N+1):
    if i%2==1:
        sum+=i
print("The sum of all odd numbers is ",sum)