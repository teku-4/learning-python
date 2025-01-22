import json
#demonstration of jeson file by contact 
def save_contacts(name,phone_number):

    contacts={
        "Name":name,
        "phone_number":phone_number}
    with open("my_contacts.json","w") as file:
        json.dump(contacts,file)
        print("jeson file is created successfully")
def adds_other_contacts(name,phnone_number):
    added_contacts={"Name":name,
                    "phone_number":phnone_number}
    with open("my_contacts.json","a") as file:
        json.dump(added_contacts,file)
        print(f"my contact: name: {added_contacts['Name']} phone number: {added_contacts['phone_number']} is added successfuly! ")
def display_contacts():
    try:
        with open("my_contacts.json","r") as file:
            contacts=json.load(file)
            print(f"the contacts are: {contacts}")
    except FileNotFoundError:
        print("this file is not created befor ")
    except json.JSONDecodeError:
        print("this raise json decorators error")
    except Exception as e:
        print(f"an error is occured : {e}")                
def main():
    while True:
        print(" A to adding contacs")
        print(" S to save contacs")
        print(" D to display contacs")
        print(" 0 to exists from the program")
        choice=input("enter your choice from the above main menu)").upper()
        if choice=="S":    
            name=input("enter your name please ")
            phone_number=input("enter your phone number please")
            save_contacts(name,phone_number)
        elif choice=="A":
            name=input("enter your name please") 
            phone_number=input("enter your phone number please")   
            adds_other_contacts(name,phone_number)
        elif choice=="D":
            display_contacts()  
        elif choice=="0":
            print("Goodbye have a nice time")
            break      
        else:
            print("please enter the valid input according to the provided option")   

if __name__=="__main__":
    main()    