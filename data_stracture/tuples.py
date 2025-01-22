# tuples_1=("apples",)
# print(type(tuples_1 ))
# tuples_2=(([x*3 for x in range(11) if x%3==0]))
# print(tuples_2)
# tuples_3=(tuples_2)
# print(tuples_3)
#unpacking tuples
# fruits_1=("mango","banana")
# x,y=fruits_1
# print(x,y)
# #if the value is mustbe match to the variable if not use *
# fruits_2= ("apple", "banana", "cherry", "strawberry", "raspberry")
# (a,b,*c)=fruits_2
# print(a)
# print(b)
# print(fruits_2)
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)
# tuples_4=("python","c++")
# print(tuples_4*2)
# #reversing tuples
# print(tuples_4[::-1])
# # Accessing Tuple with Indexing
# tup = tuple("Geeks")
# print(tup[0])

# # Accessing a range of elements using slicing
# print(tup[1:4])  
# print(tup[:3])
# tuples_5=("javascript",)
# print(tuples_5[0])
##sorted tuples
# tuples_6=(1,4,3,5,2)
# tuples_7=sorted(tuples_6)
# print(tuples_7)
# #sorted in decending order
# tulpes_8=sorted(tuples_6,reverse=1)
# # print(tulpes_8)
# tuples_in_lists=[1,2,3,(1,2,3),(5,7,98),7,8,(1,)]
# count=0
# lc=0
# for i in range(len(tuples_in_lists)):
#     if isinstance(i,tuple):
#         count+=1
#     else:
#         lc+=1
# print("the number tuples is",count )
# print("the number lists is",lc )