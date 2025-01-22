# # global variables
# number1=34
# def adds(num):
#     number2=56
#     print(f"{num}+{number2}={num+number2}")
#     print(f"{number1}+{number2}={number1+number2}")
# adds(53)
# adds()


#enclocing variable scop
# def outer(number):
#     num=30
#     def inner(nums):
#         print(f"{num}+{nums}={num+nums}")
#     inner(23)
#     print (f"{number}+{num}={num+number}")         
# outer(56)
# def calculate_area(dimention):
#     side=26
#     raduis=34
#     def square(side):
#         return side**2
#     def circle(radius):
#         return (radius**2)*3.14
#     if dimention=="squere":
#         print(f"{square(side)}")
#     elif dimention=="circle":
#         print(f"{circle(raduis)}")   
#     else:
#         print("there is no calculation for  such dimetion")    

# circles=calculate_area("circle")
# square=calculate_area("squere")
