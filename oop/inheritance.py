# #inheritace
# class Animal:
#     def __init__(self,name):
#         self.name=name
#         self.isalive=True
#     def eat(self):
#         print(f"{self.name} is eating")
#     def sleep(self):
#         print(f"{self.name} is sleeping now")
# class Dog(Animal):
#     def speak(self):
#         print("woof")
# class Cat(Animal):
#     def speak(self):
#         print("meew")
# class Mouse(Animal):
#     def speak(self):
#         print("sueq")
# dog=Dog("Max")
# print(dog.name,dog.isalive ,dog.sleep())
# cat=Cat("gafield")
# print(cat.name,cat.eat())
# mouse=Mouse("mikey")
# # print(mouse.name,"is alive",mouse.isalve)
# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def display_name(self):
#         print(f"My name is {self.fname} {self.lname}")

# # Single inheritance
# class Student(Person):
#     def __init__(self, fname, lname, year, cgpa):
#         super().__init__(fname, lname)
#         self.year = year
#         self.cgpa = cgpa

#     def welcome(self):
#         print(f"Welcome! I am {self.fname} {self.lname}.")
#         print(f"I graduated in {self.year} with a CGPA of {self.cgpa}.")

# class Job:
#     def __init__(self, salary):
#         self.salary = salary

#     @staticmethod
#     def calculate_net_salary(initial_salary, bonus):
#         net_salary = initial_salary + bonus
#         return net_salary

# # Multiple inheritance
# class Employee(Person, Job):
#     def __init__(self, fname, lname, salary, profession):
#         Person.__init__(self, fname, lname)
#         Job.__init__(self, salary)
#         self.profession = profession

#     def employee_info(self):
#         net_salary = Job.calculate_net_salary(self.salary, 2000)  # Example bonus
#         print(f"My profession is {self.profession} and my net salary is {net_salary}.")

# # Multilevel inheritance
# class Teacher(Employee):
#     def __init__(self, fname, lname, salary, course_assign):
#         Employee.__init__(self, fname, lname, salary, "Teacher")
#         self.course_assign = course_assign

#     def teach_info(self):
#         print(f"I am a {self.profession} and I am assigned to teach {self.course_assign}.")
#         net_salary = Job.calculate_net_salary(self.salary, 1500)  # Example bonus
#         print(f"My net salary is {net_salary}.")

# # Hybrid inheritance
# class Supervisor(Teacher):
#     def __init__(self, fname, lname, salary, course_assign):
#         Teacher.__init__(self, fname, lname, salary, course_assign)

#     def display_super_info(self):
#         net_salary = Job.calculate_net_salary(self.salary, 2500)  # Example bonus
#         print(f"I am a {self.profession} and my net salary is {net_salary}.")

# # Testing the classes

# # Single inheritance object
# Student1 = Student("Abel", "Kebede", 2016, 3.6)
# Student1.welcome()

# # Multiple inheritance object
# print("\nMultiple inheritance object:")
# employee = Employee("Rodas", "Tedla", 20000, "Software Developer")
# employee.employee_info()

# # Multilevel inheritance
# print("\nMultilevel inheritance object:")
# teacher = Teacher("Nata", "Girma", 13000, "Chemistry")
# teacher.teach_info()

# # Hybrid inheritance
# print("\nHybrid inheritance object:")
# supervisor = Supervisor("Dagne", "Kebede", 30000, "Supervisor")
# supervisor.display_super_info()
# #herarchical inheritance
# class Vehicle:
#     def __init__(self,wheel,color):
#         self.wheel=wheel
#         self.color=color
#     def vehcle_speed(self,speed):
#         self.speed=speed
#         return f"{self.color}: speed is {self.speed} "  
# #herarchical inheritance
# class Car(Vehicle):
#     def __init__(self, wheel, color, price):
#         super().__init__(wheel, color) 
#         self.price=price
#     def car_info(self):
#         return f"{self.color} color car is bought by {self.price} Birr" 
# class Sino_Truck(Vehicle):
#     def __init__(self, wheel, color,size ):
#         super().__init__(wheel, color) 
#         self.size=size
#     def display_truck_info(self):
#         return f"{self.color} color sino is {self.size}" 
# car=Car(4,"white",100000000)    
# print(car.car_info()) 
# sinotruck=Sino_Truck(4,"red","huge")                            
# print(sinotruck.display_truck_info())        
