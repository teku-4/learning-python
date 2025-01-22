import getpass
user_name=input("enter you user name").strip().lower()
password=getpass.getpass("Enter your password ")
if user_name=="letakasahun" and password=="leta@2369":
    print(f"you are authenticated")
else:
    print("please enter the valid password and username")    
