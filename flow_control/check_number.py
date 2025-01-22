#check even or odd
print("Even or odd")
number=int(input("Enter a number ".strip()))
if number%2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
#check positive or negative
print("positive or negatiov or zero")
if number>0:
    print(f"{number} is positive")
elif number<0:
    print(f"{number} is negative") 
else:
    print("zero")
    