import math
from functools import reduce
import statistics


def addition(number1,number2):
    return number1 + number2
def sbtraction(num1,num2):
    return num1 - num2

def multplication(frist_number,second_number):
    return frist_number * second_number

def division(fristNum,secondNum):
    choice=input("enter your wish (floor or normal) devision")
    if choice=="floor":
        return fristNum//secondNum
    elif choice=="normal":
        return fristNum/secondNum
    else:
        print("please enter according to the given option")

def modulo(numb1,numb2):
    return numb1%numb2

def exponation(number):
    exponent=int(input("enter the exponent"))
    return number**exponent

def radical(num):
     return math.sqrt(num)

def trignometric():
    choice=input("Enter your wish to calculate trig: (commen or inverse) trignometric")
    if choice=="commen":
        angle=float(input("enter the angle"))
        in_radian=math.radians(angle)
        options=input("enter your option: (sine  cosine tanget)")
        if options=="sine":
            return math.sin(in_radian)
        elif options=="cosine":
            return math.cos(in_radian)
        elif options=="tangent":
            return math.tan(in_radian)
        else:
            return "please enter the option according to the provided option"
        
    elif choice=="inverse":
        values=float(input("enter the value"))
        option=input("enter your option: (arcsine arccose arctangent)")
        if option=="arcsine":
            arcsine_value=math.asin(values)
            in_degree=math.degrees(arcsine_value)
            return  in_degree
        elif option=="arcosine":
            arcosine_value=math.acos(values)
            in_degree=math.degrees(arcosine_value)
            return  in_degree
        elif option=="arctangent":
            arctan_value=math.atan(values)
            in_degree=math.degrees(arctan_value)
            return  in_degree
        else:
            print("please enter the correct option")
    else:
        print("enter the correct choice based the given option")
def calculate_logarism():
    number=int(input("enter a nummber to calculate logarithsm"))
    options=input("enter your option(natural,common,custom)logarithm")
    if number>0:
        if options=="natural":
            #logarism in base "e"
            print( f"the natural logarisim of {number} is {math.log(number)}")
        elif options=="common":
            #log with base 10
            print((f"the common logarism of {number} is {math.log10(number)}"))
        elif options=="custom":
            base=int(input("enter the base of logarism"))
            if base >0:
                  #custums are when the base is any  number
                  print(f"the logarisms of {number} in base {base} is {math.log(number,base)}")
            else:
                print("the base must be greater than zero")
        else:
            print("please enter correctly acording to the obtion") 

def calculate_Mean():
    lists_len=int(input("enter the length of lists "))
    lists=[(numbers:=int(input("enter a number "))) for _ in range(lists_len)]
    mean=sum(lists)/lists_len
    print(f"the mean of {lists} is {mean}")

    
def calculate_Mode():
    lists_len=int(input("enter the length of lists "))
    lists=[(numbers:=int(input("enter a number "))) for _ in range(lists_len)]
    mode=statistics.mode(lists)
    print(f"the the mode of  of {lists} is {mode}")
def calculate_Range():
    lists_len=int(input("enter the length of lists "))
    lists=[(numbers:=int(input("enter a number "))) for _ in range(lists_len)]
    #finding max and min of lits to get range
    maximum=max(lists)
    minimum=min(lists)
    range=maximum-minimum
    print(f"the range of {lists} is {range}")
    
def calculate_Variance():
    lists_len=int(input("enter the length of lists "))
    lists=[(numbers:=int(input("enter a number "))) for _ in range(lists_len)]
    Variances=statistics.variance(lists)
    print(f"the variance  of {lists} is {Variances}")
def calculate_standard_devation():
    
    lists_len=int(input("enter the length of lists "))
    lists=[(numbers:=int(input("enter a number "))) for _ in range(lists_len)]
    Variances=statistics.variance(lists)
    #standard divation is simply  the square root of variance
    standard_devation=Variances**0.5
    print(f"the standard divation   of {lists} is {standard_devation}")
def calculate_Median():
    
    lists_len=int(input("enter the length of lists "))
    lists=[(numbers:=int(input("enter a number "))) for _ in range(lists_len)]
    mediance=statistics.median(lists)
    print(f"the median  of {lists} is {mediance}")
def check_comp_prime():
    number=int(input("enter the number to check composit or prime"))
    count=0
    for factors in range(1,number+1):
        if number%factors==0:
            count+=1

    if count==2:
        print("prime number")
    else:
        print("composite number")   
def calculate_greatest_common_fuctor():
    lists_len=int(input("enter the length of lists "))
    lists=[(numbers:=int(input("enter a number "))) for _ in range(lists_len)]
    gcf=reduce(math.gcd,lists)
    print(f"the gretest common fuctors of {lists} is {gcf}")
def calculate_list_common_multple():   
    
    lists_len=int(input("enter the length of lists "))
    lists=[(numbers:=int(input("enter a number "))) for _ in range(lists_len)]
    LCM=reduce(math.gcd,lists)
    print(f"the list common multple  of {lists} is {LCM}") 
#main menu
def main_menu():
        while True:        
            print("######    Ask any mathematics related calculetor ###")
            print("     ** Main Menu **")
            print("-----------------------------------------\n")
            print("     press 1: for addition:\n")
            print("     press 2: for substraction:\n")
            print("     press 3: for multiplication:\n")
            print("     press 4: for division:\n")
            print("     press 5: for modulo:\n")
            print("     press 6: for Exponansation:\n")
            print("     press 7: for Radical:\n")
            print("     press 8: for Trignometric:\n")
            print("     press 9: for logarism:\n")
            print("     press 10: for Mean:\n")
            print("     press 11: for Mode:\n")
            print("     press 12: for Range:\n")
            print("     press 13: for variance:\n")
            print("     press 14: for Standard devation:\n")
            print("     press 15: for Median:\n")
            print("     press 16: for chekc composite prime:\n")
            print("     press 17:  for greatest common fuctor:\n")
            print("     press 18: list common multple:\n")
            print("     press 0: To exit:\n")


            print("-----------------------------------------\n")



            option = int(input(" Enter your option from the above menu:"))
            match option:
                case 1:
                    num1,num2=map(int,input("Enter the number: ").split())
                    print(f"{num1} + {num2} = {addition(num1,num2)}")
                case 2:
                    numb1,numb2=map(int,input("enter the numbers").split())
                    print(f"{numb1} - {numb2} = {sbtraction(numb1,numb2)}")
                case 3:
                    number1,number2=map(int,input("enter the numbrs :").split())
                    print(f"{number1} * {number2} = {multplication(number1,number2)}")
                case 4:
                    frist_num,second_num=map(int,input("enter the numbs").split())
                    print(f"{frist_num} / {second_num} ={division(frist_num,second_num)}")
                case 5:
                    fristNumbr,secondNumber=map(int,input("enter the number").split())
                    print(f"{fristNumbr}%{secondNumber}={modulo(fristNumbr,secondNumber)}")
                case 6:
                    number=int(input("enter the number "))
                    print(f"the exponent of {number } is {exponation(number)}") 
                case 7:
                    num=int(input("enter the number"))
                    print(f"the squere root of {num} is {radical(num)}")       
                case 8:
                    print(f"The result is {trignometric(): .2f}")
                case 9:
                    calculate_logarism()
                case 10:
                    calculate_Mean()
                case 11:    
                    calculate_Mode()   
                case 12:
                    calculate_Range()
                case 13:
                    calculate_Variance()
                case 14:
                    calculate_standard_devation()
                case 15:
                    check_comp_prime()
                case 16:
                    calculate_greatest_common_fuctor()
                case 17:
                    calculate_list_common_multple()
                case 0:
                    print("Goodbye have a nice time")    
                case _:
                    print("invalid input")
main_menu()