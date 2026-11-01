num=int(input("enter a number: "))
summation=0
for i in range(0,  num+1):
    if i%2==0:
        summation+=i
    
print(summation)