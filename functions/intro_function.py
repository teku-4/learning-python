# #  Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of i
# def capitalize_lists(lists):
#     capitalized=[]
#     for itemes in lists:
#         capitalized.append(itemes.capitalize())
#     print(capitalized)
# lists=["abel","kebron","getabalew"]
# capitalize_lists(lists)
# #Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# def add_item():
#    lists1 =["potato","orange","mango"]
#    lists2=["banana","apple"]
#    lists1.append(lists2[1])
#    print(lists1)
# add_item()
# #13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# def sum_of_number(nums):
#     sum=0
#     for num in range(nums+1):
#         sum+=num
#     print(sum)

# sum_of_number(10)
# #14 write a function to addd even and odd
# def add_even_odd():
#     number=int(input("enter the number to add"))
#     sum_even=0
#     sum_odd=0
#     count_even=0
#     count_odd=0
#     for n in range(number+1):
#          if n%2==0:
#             count_even+=1
#             sum_even+=n
#          else:
#            sum_odd+=n
#            count_odd+=1
#     print(f"sum of even nuber is {sum_even}\n sumof odd number is {sum_odd}")
#     print(f"the number of eve number up to {number} is {count_even}")
#     print(F"the number of odd number up to {number}is {count_odd}")
# add_even_odd() 
# def factorial(n):
#    if n==0:
#     return 1
#    elif n<0:
#     return "the factorial should be non negative"
#    else:
#     return n*factorial(n-1)
# num=int(input("enter the to find its factorial:"))
# print(f"{num}! = {factorial(num)}")
# def check_empty(dataValue):
#     if len(dataValue)==0:
#         return True
#     else:
#         return False
# x=[]
# print(check_empty(x))
# y=[1,2,3,4]
# print(check_empty(y))