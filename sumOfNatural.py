N = int(input("Enter a positive integer: "))

sum = 0
for i in range(1, N + 1):
    sum+= i
print("Sum of natural numbers from 1 to", N, "is:", sum)
