#standard arguement
# positional argument
# def greet(name):
#     print(f"hello {name}")
# greet("Abel")
# greet("Abgel")
# greet("Samuel")


# #keyword argument
# def say_welcome(frist_name,last_name):
#     return f"welcome my name is: {frist_name} {last_name}"
# print(say_welcome(last_name="Kasahun",frist_name="leta"))


# #default argument
# def add_number(number1,number2=45,number3=60):
#     sumation=number1+number2+number3
#     return f"{number1}+{number2}+{number3}={sumation}"
# print(f"pass one arg: \n{add_number(23)}")
# print(f"pass two arg: \n{add_number(23,46)}")
# print(f"pass three arg: \n{add_number(23,78,90)}")


#varaible  number positional argument
# def my_func(*kids):
#     print("Access only one argument:",kids[1]
#           )
#     print("access two argumnet: " , kids[2])
#     print("accessing all the three arguments",kids)
# my_func("Linus","Topias","Abgel")
# def call_fruits(*fruit):
#     return fruit
# lists_fruit=["apple","mango","banana","papaya"]
# print(f"access one value:\n{call_fruits(lists_fruit[0])}")
# print(f"access two value:\n{call_fruits(lists_fruit[0:2])}")
# print(f"access three value:\n{call_fruits(lists_fruit[0:3])}")
# #varaible keyword arg
# print("access all values")
# for fruit in lists_fruit:
#     print(f"-{fruit}")


# #varables number keyword argument
# def data(**student_info):
#     for key,value in student_info.items():
#         print(f"{key}:{value}")
# data(name="abela",age=34,cgpa=4.0)        
# data(name="getu",age=33,cgpa=3.0)
# print("empty",data())


# #positional only arguments
# def tell_name_age(name="tera",/,age=90):
#     return f"I am {name} and {age} years old"
# print(tell_name_age("Abera",34))
# print(tell_name_age("Tedy",age=56))
# print(tell_name_age())



#keyword only arg
# def call_animal(*,name,color,):
#     print(name,color)
# call_animal(name="ox",color="red")


# mixed arguements
# def all_type(positional_only,/,any_type,*,keyword_only):
#     return positional_only+any_type+keyword_only
# print(all_type(20,30,keyword_only=67))
# print(all_type(20,any_type=30,keyword_only=67))


# def process_user_data(name,/,*,email,**additional):
#     print(f"name {name}")
#     print(f"email: {email}")
#     for key,value in additional.items():
#         print(f"{key}:{value}")
# process_user_data("Belal",email="bel2@gmail.com",adress="adama",phone="0987653456")    


