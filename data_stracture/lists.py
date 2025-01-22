# list1_fruits=["apple","orange","banana","mango","avocado"]
# print("lists of some fruit: ",list1_fruits)

# #list  manuplation
# #slicing
# print(list1_fruits[1:4])
# print(list1_fruits[::2])
# print(list1_fruits)
# # accessing through index
# print(list1_fruits[1])
# courses=[["principle of programming","fudamental of software engineering","database"],["SEng 2021","SEng 2031","Seng 2041"]]
# print(courses[0][0],courses[1][0])
# print(courses[0][1],courses[1][1])
# # print(courses[0][2],courses[1][2])
# empty_lists=[]
# #adding list
# empty_lists.append("frist")
# print("after appending",empty_lists)
# empty_lists.insert(1,"second")
# print("after iserting",empty_lists)
# empty_lists.extend(["third","fourth","fiveth"])
# print("after exteded",empty_lists)
#udating lists using index
# listt2_fruits=["chery","tomato"]
# listt2_fruits[1]="potato"
# print(listt2_fruits)
# list_frist_squere_number=[a**2 for a in range(1,11) if a%2==1]
# print(list_frist_squere_number)
# Removes the first occurrence of 40
# a=[10,20,30,40,50]
# a.remove(40)
# print("After remove(40):", a)

# # Removes the element at index 1 (20)
# popped_val = a.pop(1)  
# print("Popped element:", popped_val)
# print("After pop(1):", a) 
# #pop withouth specifying
# print(a.pop())
# #delet with specifying 
# del a[0]
# print(a)
# #clear the list 
# a.clear()
# print(a)
# #eleting entire list
# del a
# print(a)
# 


matrix_lists=[[1,2,3,4,5],
              [7,8,9,10],
              [11,12,13,14]]
#accesing individual element
# for a in range(len(matrix_lists)+1):
#     for b in range(len(matrix_lists)+1):
#         print(matrix_lists[a][b],end=", ")
# #flattenimng the above lists
# flatteen_lists=[]
# for a in range(len(matrix_lists)):
#     for b in range(len(matrix_lists)+1):
#         flatteen_lists.append(matrix_lists[a][b])

# print(flatteen_lists)
# print(len(matrix_lists))
# print(len(flatteen_lists))

# compressed_lists= [1, 2, [3, 4, [5, 6], 7], [[[8, 9], 10]], [11, [12, 13]]]

# #using recursive function
# def flatten_lists(lists):
#    flat_list=[]
#    for x in lists:
#       if isinstance(x,list):
#           flat_list.extend(flatten_lists(x))
#       else:
#           flat_list.append(x)

#    return flat_list
# print(flatten_lists(compressed_lists))

# print( isinstance(2,int))
#list comprehesion
##name=[expresion for itrable condition]
#sum of odd number n raised to 2
# new_lists=[x**3 for x in range(101) if not x%3==0 and not x%2==0]
# print(new_lists)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x if (x !="banana" and x!="kiwi") else "orange" for x in fruits]

# print(newlist)
# lists=[["apple","orange"],["tomato",["bana","tiger"],"penapple"]]
# flated_list=[x for item in lists  for a in item for x in a]
# print(flated_list)
#determine the number usin even or using list comprehesion
# liste_of=["Even" if x%2==0 else "Odd" for x in range(11)]
# print(liste_of)
# divisiblity=['divided by 2' if x%2==0 else "divides by 3" if x%3==0 else "other" for x in range(11) ]
# print(divisiblity)
# lists=[1,3,4,6,7,8,9,10]
# new_lists=[(x-2 for x in lists[::2])]
# print(new_lists)
##swaping in lists
lists_swaping=[10,20,30,40,50,60,1,3,70,80,90,100]
# print("before swaping: ",lists_swaping)
# temp=lists_swaping[0]
# lists_swaping[0]=lists_swaping[1]
# lists_swaping[1]=temp
# print(lists_swaping)
# lists_swaping[0],lists_swaping[-1]=lists_swaping[-1],lists_swaping[0]
# # print(lists_swaping)
# reversed_lits=[]
# #copyin lists
# reversed_lits=lists_swaping.copy()
# print("copied lits: ",reversed_lits)
# reversed_lits.reverse()
# print("revresing :",reversed_lits )
# count=0
# for i in reversed_lits:
#     if i%2==0:
#       count+=1
      
# print(count)
lifsts_number=[12,34,56,57.8,9.6]
greeatest=map(filter((lambda x,y:y if y>x else x),lifsts_number),lifsts_number)
print(greeatest)
    