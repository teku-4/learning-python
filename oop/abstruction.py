from abc import ABC, abstractmethod 
import math

# class Computor(ABC):
#     @abstractmethod
#     def proccess(self):
#         pass
# class Laptop(Computor):
#     def proccess(self):
#         print("the proccessing system of laptop")
# class Desctop(Computor):
#     def proccess(self):
#         print("the proccessing system of desctop")
# desctop1=Desctop()
# desctop1.proccess()
# laptop1=Laptop()
# laptop1.proccess()                  
#area calcution usigabstruct concepts

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#            self.radius=radius
#     def area(self):       
#            print (f"the are of circle is {(self.radius**2)*math.pi}")
   
# class Rectangle(Shape):
#     def __init__(self,length , width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print (f"the area of rectangle is {self.width*self.length}")
# class Square(Shape):
#     def __init__(self,length):
#         self.length=length
#     def area(self):
#         print(f"the area of square is {self.length**2}")
# option=int(input("enter your optio (1. to area of circle, \n 2. for area of rectangle\n 3. for area of square)"))                
# while True:   
#     match option: 
#         case 1:
#             radius=float(input("enr the radius of circle"))
#             circle=Circle(radius)  
#             circle.area() 
#         case 2:
#             length=int(input("enter the length of rectangle: "))
#             width=int(input("enter the width of rectangle"))
#             rectangle=Rectangle(length,width) 
#         case 3:
#             length_sq=int(input("enter the length of square "))
#             square=Square(length_sq)
#             square.area()
#         case _4:
#             print("enter the correct option")  
#             break         
            
class Animal(ABC):
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    @abstractmethod
    def make_sound(self):
        pass
class Cat(Animal):
    def __init__(self,name,sound,age):
        super().__init__(name,sound)
        self.age=age
    def make_sound(self):
        print(f"{self.name}  says {self.sound} and {self.age} years old")    
class Donkey(Animal):
    
    def __init__(self,name,sound,age):
        super().__init__(name,sound)
        self.age=age
    def make_sound(self):
        print(f"{self.name}  says {self.sound} and {self.age}years old ")
    
class Dog(Animal):
    def __init__(self,name,sound,age):
        super().__init__(name,sound)
        self.age=age
    def make_sound(self):
        print(f"{self.name}  says {self.sound} and {self.age}years old ")
    
cat=Cat("cat","mew",1)
cat.make_sound()
dog=Dog("puppy","woof",4)   
dog.make_sound() 
donkey=Donkey("donkey","hahaha",12)
donkey.make_sound()