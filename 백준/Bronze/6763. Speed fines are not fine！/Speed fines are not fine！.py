limit = int(input())
speed = int(input())
res = speed - limit
if 1<= res <= 20:
    print("You are speeding and your fine is $100.")
elif 21<= res <=30:
    print("You are speeding and your fine is $270.")
elif 31<=res:
    print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")