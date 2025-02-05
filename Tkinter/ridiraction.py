import tkinter as tk
from tkinter import messagebox

def registration_form():
    root = tk.Tk()
    root.title("Registration Form")
    root.geometry("400x400")
    name="Ababe"
    email="abebe@gmail.com"
    passwords="1123abe"
    name_value = name_entry.get()
    email_value = email_entry.get()
    password_value = password_entry.get()
    gender_value = sex_value.get()
    age_value_selected = age_value.get()
    department_value = depart.get()
    selected_skills = [hobbies[i] for i in range(len(hobbies)) if hobi_var[i].get()]
    
    messagebox.showinfo(title="Submitted", message=f"Name: {name_value}\nEmail: {email_value}\nDepartment: {department_value}\nSkills: {', '.join(selected_skills)}")

    tk.Label(root, text="ENTER THE FOLLOWING FORM", font=("Arial", 20, "bold"), padx=5, pady=5, bg="black", fg="aqua").grid(column=1, row=1, columnspan=2)

    tk.Label(root, text="Enter name:").grid(row=2, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=2, column=1)

    tk.Label(root, text="Enter Email:").grid(row=4, column=0)
    email_entry = tk.Entry(root)
    email_entry.grid(row=4, column=1)

    tk.Label(root, text="Enter password:").grid(row=6, column=0)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=6, column=1)

    tk.Label(root, text="Enter gender:").grid(row=8, column=0)
    sex_value = tk.StringVar(value="male")
    male_radio = tk.Radiobutton(root, text="Male", variable=sex_value, value="male")
    male_radio.grid(row=8, column=1)
    female_radio =tk.Radiobutton(root, text="Female", variable=sex_value, value="female")
    female_radio.grid(row=8, column=2)

    tk.Label(root, text="Enter age:").grid(row=10, column=0)
    age_value = tk.IntVar(value=0)
    age = tk.Spinbox(root, from_=0, to=100, textvariable=age_value)
    age.grid(row=10, column=1)

    tk.Label(root, text="Enter department:").grid(row=12, column=0)
    depart = tk.StringVar(value="select department")  # Correctly initialized as StringVar
    departments = ["IT", "SE", "IS", "EE", "ME", "CS", "DS"]
    department_menu = tk.OptionMenu(root, depart, *departments)
    department_menu.grid(row=12, column=1)

    hobbies = ["Influencing", "Communication", "Technical Skill", "Negotiating"]
    hobi_var = [tk.IntVar() for _ in hobbies]
    hobbies_frame = tk.LabelFrame(root, text="Select Your Skills:", padx=20, pady=20)
    hobbies_frame.grid(row=14, column=1)

    for i, skill in enumerate(hobbies):
        check = tk.Checkbutton(hobbies_frame, text=skill, variable=hobi_var[i])
        check.grid(row=i, column=0, sticky='w')

    # Buttons
    submit = tk.Button(root, text="Register", font=("Arial", 20, "bold"), command=registration_form)
    submit.grid(row=24, column=1)
    root.mainloop()

log=tk.Tk()
log.title("login")
log.geometry("200x200")
def login_form():
    username="letakasahun"
    password="1234leta"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="login",message="you loged in succesffuly")
        log.destroy()
        registration_form()
        
    else:
        messagebox.showerror(title="login",message="incorrect password and username")    
def backspace_form():
    if username_entry.get():
        username_entry.delete(len(username_entry.get())-1)  
    elif password_entry.get():
        password_entry.delete(len(password_entry.get())-1)  

tk.Label(log,text="Fill information").grid(row=0,columnspan=2)
tk.Label(log, text="username:").grid(row=1,column=0)
username_entry=tk.Entry(log)
username_entry.grid(row=1,column=1)
tk.Label(log,text="Password:").grid(row=5,column=0)
password_entry=tk.Entry(log,show="*")
password_entry.grid(row=5,column=1)
login_button=tk.Button(log,text="Login",font=("Arial",20,"bold"),padx=4,pady=4,bg="black",fg="white",command=login_form)
login_button.grid(row=10,column=0)
backspace=tk.Button(log,text="Backspace",font=("Arial",20,"bold"),padx=4,pady=4,bg="black",fg="white",command=backspace_form)
backspace.grid(row=10,column=1)
log.mainloop()
