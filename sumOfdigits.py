N = int(input("Enter an integer: "))
sum=0
while N>0:
    rem=N%10
    sum+=rem
    N=N//10
print("The sum of digits is :",sum)