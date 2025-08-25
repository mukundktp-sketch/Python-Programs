a=int(input("enter the number for the day: "))
if(a<=1 or a<=7):
    days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
    }
    print("day is: ", days.get(a))
else: 
    print("enter valid number of day")