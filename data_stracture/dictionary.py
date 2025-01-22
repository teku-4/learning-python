
# car=dict(model="mustang",brand="ford",year=1978)
# print(car)
# #accessing dictionary
# print(car["model"])
# print(car.get("brand"))
# print(car.keys())
# print(car.values())
# print(car.items())
# #difference is only the get is not error prone because if attempt to access doen't exit idex it return none
# print(car.get("color"))#output 
# #updating dictionary
# car["year"]=2003
# print(car)
# #adding values
# car["colo"]="red"
# print(car)
# #rmovedictionary
# del car["colo"]
# print("color is deleted",car)
# poped=car.pop("year")
# print("the year is poped ",car)
# car.clear()
# # print(car)
# try:
#     programming_langge={1:"python",2:"java",3:"c++",4:"sql",5:"html"}
#     for value in programming_langge.values():
#         print(value)
#     for key in programming_langge.keys():
#         print(key)
#     for i,j in programming_langge.items():
#         print( i,":",j  ) 
#     #copyng dictionary
#     copied_dictionary=programming_langge.copy()
#     print("the copied dictionary is",copied_dictionary)
#     poped_item=copied_dictionary.popitem()
#     print("the poped dictionary is",poped_item)
#     #nested dictionary
#     all_students={"student1":{"name":"abel","age":22,"mark":[78,90,60]},
#                 "student2":{"name":"abat","age":21,"mark":[88,90,60]},
#                 "student3":{"name":"abera","age":20,"mark":[78,989,60]}
#                 }
#     print(all_students["student1"])
# except Exception as a:
#     print("the proble is due the error of",a)
#geting maxim values dictionary
# Python code to find key with Maximum value in Dictionary
 
# Dictionary Initialization
# listss=[]
# Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88}
# # listss.extend(Tv.values())
# # print(listss)
# Keymax = max(Tv,key= lambda x: Tv[x])
# print(Keymax)
# # lists=[]
# for i in range(3):
#     name=input("what is your name ")
#     dep=input("deparment  ")
#     work=int(input("wourk exprience "))
#     cgpa=float(input("cgpa  "))
#     data={
#         "Name":name,
#         "depar":dep,
#         "works":work,
#         "CGPA":cgpa
#     }
#     lists.append(data)

# print(lists)
# r=int(input("enter the raduis"))
# cr=lambda r:(r**2)*3.143
# ##avoiding duplicates values
original_dict={"maths":90,"chem":90,"phy":96,"hitory":68}
# max_mark=max(original_dict,key=lambda x: original_dict[x])
# print(max_mark)
# res = dict()
# temp=[]
# for key, val in original_dict.items():

# 	if val not in temp:
# 		temp.append(val)
# 		res[key] = val

# print("original dictionary",original_dict)
# print("filtered dictionary is",res)
#avoiding duplicates using comptrension
temp={key:value for key,value in original_dict.items()}
result={key:value for key,value in temp.items()}
print("the  original is ",original_dict)
print("the filtered dict is " , result)
# initializing dictionary
test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Remove duplicate values in dictionary
# Using dictionary comprehension
temp = {val: key for key, val in test_dict.items()}
res = {val: key for key, val in temp.items()}

# printing result
print("The dictionary after values removal : " + str(res))
#lambda functionanonemous functino tha retur only on expression 
#using lambda fuction returning the number squer after doubling it
def myFunc(number):
   return lambda a:a*number

doblerNumber=myFunc(4)
print(doblerNumber(3))
