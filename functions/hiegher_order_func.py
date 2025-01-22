# # def Apply_func(func,value):
# #     return func(value)
# # def cube(number):
# #     return number**3
# # number=int(input("enter the number")
# #            )
# # print(f"{number} the powre of 3 is {Apply_func(cube,number)}")

# # function using map 
# #celcies to faranite
# # temp_cel=[0,32,37,100]
# # temp_franites=map(lambda c:(c*9/5)+32,temp_cel )
# # temp_faranites=list(temp_franites)
# # print(f"{temp_cel}celcies is {temp_faranites} in franites")


# # strings=["apples","banana","avocado"]
# # len_strings=map(len,strings)
# # print(list(len_strings))
# # #convertin to uppercase
# # upper_lists=map(str.capitalize,strings)
# # print(list(upper_lists))

# # lists1=[1,2,3,5]
# # lists3=[5,6,7,8]
# # lists2=[3,2,4,5]
# # lists_sum=map(lambda x,y,z:x+z+y,lists1,lists2,lists3)
# # print(f" {lists1} + {lists2}+{lists3}={list(lists_sum)}")


# marks_studs=[(mark:=float(input("enter the mark of students"))) for _ in range(5)]
# filtered=filter(lambda x: x>80,marks_studs)
# print(f"the students who score greater than 80 is {list(filtered)}")

# filter the string by lengs
# words = ["apple", "banana", "cherry", "date", "fig", "grape"]
# lists_len4=filter(lambda x:len(x)>4 ,words)
# print(f"the lists of fruit thier length greater than 4 is: {list(lists_len4)}")

#filtering best candidate using lists
candidates = [
    {"name": "Alice", "experience": 5, "marks": 85},
    {"name": "Bob", "experience": 2, "marks": 92},
    {"name": "Charlie", "experience": 7, "marks": 78},
    {"name": "Diana", "experience": 4, "marks": 88}]
for candidate in candidates:
    candidate['mean_score']=(candidate['experience']+candidate['marks'])/2
filtered_candidates=sorted(candidates,key= lambda x: x['mean_score'],reverse=True)
if filtered_candidates:
    best_candidate=filtered_candidates[0]
    print("Best candidate")
    print(f"name: {best_candidate['name']}")
    print(f"exprince: {best_candidate['experience']}")
    print(f"marks: {best_candidate['marks']}")
else:
    print("no candidates")    
    