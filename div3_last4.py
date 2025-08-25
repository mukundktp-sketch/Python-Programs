num=int(input("Enter a number:"))
rem=num%10
print("Yes! The number is divisible by 03 with last digit 04" if (num%3==0 and rem==4) else "No! The number is not divisble by 03 with last digit 4")
if (num%3==0 and rem==4):
    print("Yes! The number is divisible by 03 with last digit 04")
else:
    print("No! The number is not divisble by 03 with last digit 4")