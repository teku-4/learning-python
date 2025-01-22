# def greet(name):
#     return f"hellow I am {name}"
# name=input("enter your name please ")
# print(greet(name))

# listing the prime number
def prime(number):
    
    
    for i in range(2, int(number**0.5)+1):
        if number%i==0:
            return False
    return True
def main():
    lists_prime=[]


    limit_number=int(input("enter the number to lits prim number up to you want"))
    for number in range(2,limit_number):

        if prime(number):
         lists_prime.append(number)
        
    print(f"the lits of prme number from 2 upto {limit_number} is {lists_prime}")
if __name__ == "__main__":
 main()

