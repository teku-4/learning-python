# class Car:
#     #class attribues 
#     model="Toyota"
#     def  __init__(self,color,speed,price):
#             #instance attribute
#             self.color=color
#             self.speed=speed
#             self.pice=price
#     #method
#     def start(self) :
#           return f"{self.color} is started to go"
#     def stop(self,place):
#           self.place=place
#           return f"{self.color} car is stoped at {self.place}"
# car1=Car("red",200,"100000.0")   
# car2=Car("white",300,"100000.0")
# car3=Car("blue",400,"100000.0")
# car4=Car("black",200,"100000.0")  
# print(car1.model,car1.start())  
# print(car2.stop("somewhere")) 
# class Dog:
#     species="caniene"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# dog1=Dog("bubby",4) 
# dog2=Dog("Charlie",5)
# print('this is dog1:',dog1.species,dog1.name,dog1.age)  
# print('this is dog2:',dog2.species,dog2.name,dog1.age) 
# #modificaton of class
# dog3=Dog("Max",6)
# dog3.species="Feline"  
# print("this is dog 3",dog3.species,dog3.name,dog3.age)
#basic prnciple of oop in python
#class method, instance methode and stai methode
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     #nstance methode
#     def bark(self):
#         return f"{self.name} says woof!" 
# class Dog(Animal):
#     species="canien"
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age
#     #class methd    
#     @classmethod
#     def change_species(cls,new_speceis,eat):
#         cls.species=new_speceis 
#         cls.eat=eat
#         return f"This dog eats {cls.eat} and its species is {cls.change_species}"      
# dog=Dog("puppy",4)  
# print(dog.change_species("familirse","meat"))  
# class math:
#     #statics
#     @staticmethod
#     def add(number1,number2):
#         return number2 + number1
#     @staticmethod
#     def substruct(number1,number2):
#         return number1 - number2
# calculation1=math()
# print("the divtion is",calculation1.add(23,45),"the sbstruction is",calculation1.substruct(45,23))
#all types of methonde in one class
# class Shape:
#     shapes_created = 0  # Class attribute

#     def __init__(self, name):
#         self.name = name
#         Shape.shapes_created += 1

#     def describe(self):
#         # Instance method
#         return f"This is a {self.name}."

#     @classmethod
#     def total_shapes(cls):
#         # Class method
#         return f"Total shapes created: {cls.shapes_created}"

#     @staticmethod
#     def is_polygon(sides):
#         # Static method
#         return sides >= 3

# # Creating objects
# circle = Shape("Circle")
# square = Shape("Square")

# # Using instance methods
# print(circle.describe())  
# print(square.describe())  

# # Using class methods
# print(Shape.total_shapes())  

# # Using static methods
# print(Shape.is_polygon(4))  
# # print(Shape.is_polygon(2))   
# class Item:
#     pay_rate=0.8
#     def __init__(self,name, price,quantity):
#         #validates the real value of prce and quntity
#         assert price>=0, print(f"you entered {price } is not greater than zeo")
#         assert quantity>=0, print(f"your entered quantity value {quantity} is no graeter than zero")
#         self.name=name
#         self.price=price
#         self.quantity=quantity

#     print("hello world")
#     def calculate_total_price(self):
#         return self.price*self.quantity
#     def apply_percentage(self):
#         return self.price* Item.pay_rate
# price=int(input("enter the price"))
# quantity=int(input("enter the quatity of items"))
# item1=Item("mobile",price,quantity)    
# print("he otal price of all quantty is : ",item1.calculate_total_price())
# print("he otal price of all quantty is : ",item1.apply_percentage())
# item2=Item("Laptop",100000,4)
# Item.pay_rate=0.5
# print("he otal price of all quantty is : ",item2.apply_percentage())
#control the string return value using __str__
class person:
    def __init__(abc,name,age):
        abc.name=name
        abc.age=age

    def __str__(abc):    
        return f" {abc.name} {abc.age}"
person1=person("ABE",33)    
print(person1.name,person1.age)
