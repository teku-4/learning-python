# #the same methode with different class or implimantation
# #car,plane,boat,and person
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def Move(self):
#         print(f"{self.name} walks!") 
# class Plane:
#     def __init__(self,brand):
#         self.brand=brand
#     def Move(self):
#         print(f"this {self.brand} brand plane good at FLY!")
# class Boat:
#     def __init__(self,brand):
#         self.brand=brand
#     def Move(self):
#         print(f"This {self.brand} brand boat is good at Sail!")
# class Car:
#     def __init__(self,brand):
#         self.brand=brand            
#     def Move(self):
#         print(f"This {self.brand} brand car is good at Drive!")
# #the same move() function uses or implmanted differently with different class
# person1=Person("David")
# plane1=Plane("Boeing")
# boat1=Boat("Ibiza")
# car1=Car("Ford") 
# #calling functiion at once
# for calling in(person1,plane1,boat1,car1):
#     calling.Move()
# types of polymorfism with inheritance:
#run_time polymerfism
# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     #Method overriding parrent method
#     def sound(self):
#         print("dog says woof")  

# class cat(Animal):
#     def sound(self):
#         print("cat says meaw!")
# class Sheep(Animal):
#     def sound(self):
#         print("Sheep says baaa!")


# animals=[Dog(),cat(),Sheep()]
# for animal in animals:
#     animal.sound()
#compile time polymerfisim
# class Calculate:
#     def __init__(self):
#         pass
#     def add(self,sumation,number1,number2=0,number3=0):
#         self.number1=number1
#         self.number2=number2
#         self.number3=number3
#         self.sumation=sumation
#         self.sumation=self.number1 +self.number2 + self.number3
# #method of overloading
# calculate=Calculate()
# #with one argument 0 is default for sum
# print(f"sum={calculate.add(0,4)}")

# #with two argument
# print(f"sum ={calculate.add(0,4,5)}")

# #with three arguments
# print(f"sum={calculate.add(0,4,5,6)}")


