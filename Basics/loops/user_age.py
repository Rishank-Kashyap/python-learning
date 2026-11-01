user_age = int(input("Enter your age:"))
if user_age<=13:
    print("Child")
elif 13<user_age<=19:
    print("Teenager")
elif (19<user_age<=59):
    print("Adult")
else:
    print("Senior")
    