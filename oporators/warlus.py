# Walrus Operator Examples
print("Walrus Operator Examples:")
#multply by 10 and plus 100 in one line
a=(b:=45*10)+100  
print(f"(b:=45*10)+100 ={a}")

#  Assign and check condition in one step
if (number := 10) > 5:
    print(f"(number := 10) -> number = {number} (checked and assigned in the same line)")

#Assign and use in a while loop
while (number:=int(input("enter a number except zero ")))!=0:
    print(number)
#accepts lists data type from the user
lists=[(numbers:=int(input("enter a numbers:"))) for _ in range(3)]
print(f"lists of number: {lists}")    

#  Assign and use in a comprehension
values = [1, 2, 3, 4]
squared_values = [squared := x**2 for x in values]
print(f"[squared := x**2 for x in values] -> squared_values = {squared_values}")

# Example 4: Assign and print in one line
print(f"Assigned and printed: (result := 25 * 4) -> result = {(result := 25 * 4)}")

# Example 5: Assign and use in a function call
def double(value):
    return value * 2

print(f"double((val := 10)) -> {double(val := 10)} (val = {val})")

