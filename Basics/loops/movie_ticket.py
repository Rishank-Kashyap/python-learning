user_age = int(input("Enter your age: "))
day = input("What day is today: ")

# if day=="Wednesday":
#     discount=2

discount = 2 if day == "Wednesday" else 0

# if user_age<18:
#     price=8
# else:
#     price=12

price = 12 if user_age > 18 else 8

print("Ticket price for you is $", price - discount)
