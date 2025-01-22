# class public:
#     def __init__(self,name):
#         self.name=name #publc name
#     def  display_info(self):  #public method
#         return f"hello I am {self.name}"
# person =public("abebe")
# print(person.display_info(),person.name)   
            
# #protected concepts 
# class protected:
#     def __init__(self,stud_data):
#         self._stud_data=stud_data #protected with one underscore
#     def _display_stud_data(self):
#         print(f"this is student data:\n{self._stud_data}")
# students_data={
#     "name":input("what is your name?:"),
#     "age":int(input("how old are you?")),
#     "mark":float(input("enter your mark?"))
# }        
# student1=protected(students_data)
# student1._display_stud_data            
# class private:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary #privates attributs
#     def __display_info(self): #private method
#         return f"{self.name} salary is {self.__salary}" #accecble
    
# employee1=private("kebede",55000)
# #accessed by name mangling
# print(employee1._private__display_info())    
#access dynamically by getattr(object,"_classNmae__methodName")
# employee1=private("Abel Mamo",30000)
# private_method=getattr(employee1,"_private__display_info")
# print(private_method())
