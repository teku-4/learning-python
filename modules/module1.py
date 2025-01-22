def calculate_factorial(n):
    if n>0:
        return n*calculate_factorial(n-1)
    elif n==0:
        return 1
    else:
       
        print("there is no negative factorial")
n=int(input("enter the number ot calculate"))        
print(f"{n}! = {calculate_factorial(n)}")        
if __name__=="main":
    calculate_factorial(n)