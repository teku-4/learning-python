# with open("introduction.txt","x") as file:
#     file.write("This is the introduction to file handling\n\
#                since the file if doesnot exists befor this it created by 'x' mode\n\
#              because 'x' modes is used to create file when the fie does not exists")
# with open("image.jpg","rb") as file:
#   print(file.read())
#   print("image is displayed successfulyy")

# #reading file
# with open ("introduction.txt","r") as file:
#     display_text=file.read()
#     print(display_text)

# #adding file
# with open("introduction.txt","a") as file:
#     file.write("\n Tis file is appended by using 'a mode of opration to the existing file.")

# Adding list to the file by critical mehtod
# with open("lists.txt","w") as file:
#     lits_number=[1,2,3,4,5,6,7,8,9,10]
#     file.write(''.join (str(lits_number)))

#reading lists from a file
# with open("lists.txt","r") as  file:
# #     print(file.read())

#creats file  by using dictionary
# with open ("data.txt","w") as student_data:
#     stud_data=dict(name="Abgel",age=23,cgpa=4.0)
#     student_data.write(str(stud_data))

#creats file by  dictinary data for employees by accepting the data from the user
with open("Employee_info.txt", "w") as file:
    employee_info = {
        "Name": input("Enter your name please: "),
        "Work Experience": int(input("Enter your work experience: ")),
        "CGPA": float(input("Enter your cumulative GPA please: ")),
        "Address": input("Enter your address please: ")
    }
    
    # Convert the dictionary to string format for writing
    file.write(str(employee_info))
    print("Saved successfully!")
