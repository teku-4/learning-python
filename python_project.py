# Import necessary libraries r my project
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from tkinter import font as tkfont
import pyodbc #  database integration
from datetime import datetime 

# ============= Database Configuration =============
def create_connection():
    """Creates and returns a database connection."""
    try:
        conn = pyodbc.connect(
            r'DRIVER={SQL Server};' 
            r'SERVER=DESKTOP-7SISEMO\SQLEXPRESS;'
            r'DATABASE=STMS;'
            r'Trusted_Connection=True;'
        )
        print("Database successfully connected")   
        conn.autocommit = True
        return conn
    except pyodbc.Error as ex:
        messagebox.showerror("Database Connection Error", f"Could not connect to the database: {ex}")
        return 
#----------------------------------------------------------------

def execute_query(conn, query, params=None):
    """Executes a SQL query with optional parameters."""
    if not conn:
        messagebox.showerror("Database Error", "No active database connection")
        return None
    
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        return cursor
    except pyodbc.Error as ex:
        messagebox.showerror("Database Query Error", f"Query failed: {ex}")
        return None


# ============ Classes student  =============
class student:
    """Represents a student."""
    def __init__(self, student_id, username, password, email, first_name, last_name,age,sex, department, year, semester):
        self.student_id=student_id
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.department = department
        self.year = year
        self.semester = semester

# ============ Admin Class =============
class Admin:
    """Represents an administrator."""
    def __init__(self, admin_id, username, password, email, first_name, last_name, sex,age, position):
        self.admin_id = admin_id
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.position = position
    
# ============= Complaint Class =============
class Complaint:
    """Class representing a complaint."""
    def __init__(self, complaint_id,admin_id, student_id, description, category, status, submission_date, 
                 assigned_to, resolution_details, resolution_date):
        self.complaint_id = complaint_id
        self.admin_id = admin_id
        self.student_id = student_id
        self.description = description
        self.category = category
        self.status = status
        self.submission_date = submission_date
        self.assigned_to = assigned_to
        self.resolution_details = resolution_details
        self.resolution_date = resolution_date

# ============= basic appilication =============
class ComplaintManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Complaint Management System")
        self.root.geometry("400x400")
        self.conn = create_connection()   # database impelmentation


        # Custom colors and fonts
#----------------------- colors and  fonts  --------------------
        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.button_bg = "#3498db"
        self.button_fg = "#ffffff"
        self.font_style = ("Helvetica", 14)
        self.title_font = ("Helvetica", 18, "bold")

#--------------------------- configure the main appilcation window-------------------------------------       
        self.root.configure(bg=self.bg_color)
        self.create_widgets()
    
#--------------------------- create the widgets for graphical user interface --------------------------------
    def create_widgets(self):

#--------------------------------------  title label-----------------------------------------------------------------
        self.title_label = tk.Label(self.root, text="welcome to student Complaint Management System", font=self.title_font, bg=self.bg_color, fg="lightgreen")
        self.title_label.pack(pady=(20, 10))
#---------------------------------------------------------------user name entry---------------------------------------------------------------
        self.username_label = tk.Label( self.root,  text="Username:", font=self.font_style, bg=self.bg_color, fg=self.fg_color)
        self.username_label.pack(pady=(10, 0))
        self.username_entry = tk.Entry(self.root, font=self.font_style, width=25, bg=self.fg_color, fg="#2c3e50", relief=tk.FLAT)
        self.username_entry.pack(pady=5)
#----------------------------------------------------------------password entry------------------------
        self.password_label = tk.Label( self.root, text="Password:",font=self.font_style,  bg=self.bg_color,  fg=self.fg_color)
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, font=self.font_style,  width=25,  show="*",  bg=self.fg_color, fg="#2c3e50",  relief=tk.FLAT)
        self.password_entry.pack(pady=5)

#----------------------------------------------------------------role selection combo box ---------------------------------
        self.role_label = tk.Label(self.root,  text="Role:", font=self.font_style, bg=self.bg_color, fg=self.fg_color)
        self.role_label.pack()
        self.role_combobox = ttk.Combobox(self.root,  values=["Student", "Admin"], font=self.font_style, state="readonly")
        self.role_combobox.pack(pady=5)


#---------------------------------------------------------------- button frame----------------     
        self.button_frame = tk.Frame(self.root, bg=self.bg_color)
        self.button_frame.pack(pady=10)

        
#---------------------------------------------------------------- sign in  buttons--------------  
        self.sign_in_button = tk.Button(self.button_frame, text="Sign In", font=self.font_style, bg=self.button_bg, fg=self.button_fg, relief=tk.FLAT, padx=10, pady=5,
                                         command=self.sign_in
        )
        self.sign_in_button.grid(row=0, column=0, padx=5)

#---------------------------------------------------------------- sign up  buttons--------------  

        self.sign_up_button = tk.Button( self.button_frame, text="Sign Up", font=self.font_style, bg=self.button_bg,  fg=self.button_fg,  relief=tk.FLAT,  padx=10, pady=5, 
            command=self.sign_up
        )
        self.sign_up_button.grid(row=0, column=1, padx=5)
#---------------------------------------------------------------- clear   buttons--------------  

        self.clear_button = tk.Button(self.button_frame, text="Clear", font=self.font_style, bg="#e74c3c",fg=self.button_fg, relief=tk.FLAT,  padx=10,  pady=5, 
            command=self.clear_fields
        )
        self.clear_button.grid(row=0, column=2, padx=5)
    

#------------------------------------ sign in method------------------------------------------ 
#================================================================================================   
    def sign_in(self):
        try:
            username = self.username_entry.get()
            password = self.password_entry.get()
            role = self.role_combobox.get()

            if not username or not password or not role:
                raise ValueError("All fields must be filled!")
            

            cursor = self.conn.cursor()
            table = "student" if role == "Student" else "admin"
            query = f"SELECT * FROM {table} WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            cursor.close()

            if user:
                self.root.destroy()  # Close login window
                
                if role == "Student":
                    student_id = user[0]
                    first_name = user[4]
                    dashboard_root = tk.Tk()
                    StudentDashboard(dashboard_root, student_id, self.conn, first_name)
                else:
                    admin_id = user[0]
                    first_name = user[4]
                    dashboard_root = tk.Tk()
                    AdminDashboard(dashboard_root, admin_id, self.conn, first_name)
                    
                dashboard_root.mainloop()
            else:
                messagebox.showerror("Error", "Invalid credentials or not registered!")

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except pyodbc.Error as e:
            messagebox.showerror("Database Error", f"Authentication failed: {str(e)}")


#------------------------------------ sign up method------------------------------------------


    def sign_up(self):
        role = self.role_combobox.get()
        if role == "Student":
            self.show_student_registration_form()
        elif role == "Admin":
            self.show_admin_registration_form()
        else:
            messagebox.showerror("Error", "Please select a role!")

#----------------------------------------- show student registration form------------------------------------

    def show_student_registration_form(self):
        self.root.withdraw()
        student_registration_window = tk.Toplevel()
        # FIX: Added self as second parameter
        StudentRegistrationForm(student_registration_window, self, self.conn)

#----------------------------------------------------------------show admin regestration form -------------  
    def show_admin_registration_form(self):
        self.root.withdraw()
        admin_registration_window = tk.Toplevel()
        # FIX: Added self as second parameter
        AdminRegistrationForm(admin_registration_window, self, self.conn)

#----------------------------------------- clear fields ------------------------------------
    def clear_fields(self):
        try:
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.role_combobox.set("")
        except Exception as e:
            messagebox.showerror("Error", str(e))



#================================================================ student regestration form================================================================
class StudentRegistrationForm:
    def __init__(self, root, main_app, conn):  # FIX: Added third parameter
        self.root = root
        self.main_app = main_app
        self.conn = conn
        self.root.title("Student Registration Form ")
        self.root.geometry("500x600")
    

        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.button_bg = "#3498db"
        self.button_fg = "#ffffff"
        self.font_style = ("Helvetica", 12)
        self.title_font = ("Helvetica", 16, "bold")

        self.root.configure(bg=self.bg_color)
        self.create_widgets()


#---------------- create student regestration widget--------------------------------------------------------
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Student Registration Form", font=self.title_font,bg=self.bg_color,fg="lightgreen")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # Student ID
        self.student_id_label = tk.Label(self.root,text="Student ID:", font=self.font_style,bg=self.bg_color,fg=self.fg_color)
        self.student_id_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.student_id_entry = tk.Entry(self.root,font=self.font_style,width=25,bg=self.fg_color,fg="#2c3e50",relief=tk.FLAT)
        self.student_id_entry.grid(row=1, column=1, padx=10, pady=5)

       # Username
        self.username_label = tk.Label(self.root, text="Username:", font=self.font_style, bg=self.bg_color, fg=self.fg_color)
        self.username_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = tk.Entry(self.root,font=self.font_style,width=25,bg=self.fg_color,fg="#2c3e50",relief=tk.FLAT)
        self.username_entry.grid(row=2, column=1, padx=10, pady=5)

        # Password
        self.password_label = tk.Label(self.root,text="Password:", font=self.font_style, bg=self.bg_color,fg=self.fg_color)
        self.password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.root,font=self.font_style,width=25,show="*",bg=self.fg_color,fg="#2c3e50",relief=tk.FLAT)
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        # Email
        self.email_label = tk.Label(self.root,text="Email:",font=self.font_style,bg=self.bg_color,fg=self.fg_color)
        self.email_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry( self.root, font=self.font_style,width=25,bg=self.fg_color,fg="#2c3e50",relief=tk.FLAT)
        self.email_entry.grid(row=4, column=1, padx=10, pady=5)

        # First Name
        self.first_name_label = tk.Label(self.root,text="First Name:",font=self.font_style,bg=self.bg_color,fg=self.fg_color )
        self.first_name_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.first_name_entry = tk.Entry( self.root,font=self.font_style,width=25,bg=self.fg_color,fg="#2c3e50",relief=tk.FLAT)
        self.first_name_entry.grid(row=5, column=1, padx=10, pady=5)

        # Last Name
        self.last_name_label = tk.Label(self.root, text="Last Name:", font=self.font_style, bg=self.bg_color,fg=self.fg_color )
        self.last_name_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.last_name_entry = tk.Entry(self.root,font=self.font_style,width=25, bg=self.fg_color, fg="#2c3e50", relief=tk.FLAT)
        self.last_name_entry.grid(row=6, column=1, padx=10, pady=5)

        # Age (Spinbox)
        self.age_label = tk.Label(self.root,text="Age:",font=self.font_style,bg=self.bg_color,fg=self.fg_color)
        self.age_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.age_spinbox = tk.Spinbox(self.root,from_=1,to=100,font=self.font_style,bg=self.fg_color, fg="#2c3e50",relief=tk.FLAT )
        self.age_spinbox.grid(row=7, column=1, padx=10, pady=5)

        # Sex (Radio Buttons)
        self.sex_label = tk.Label( self.root, text="Sex:",font=self.font_style,bg=self.bg_color,fg=self.fg_color)
        self.sex_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.sex_var = tk.StringVar(value="Male")  # Initialize with a default value
        self.male_radio = tk.Radiobutton(self.root,text="Male",variable=self.sex_var,value="Male",font=self.font_style,bg=self.bg_color, fg=self.fg_color)
        self.male_radio.grid(row=8, column=1, padx=10, pady=5, sticky="w")
        self.female_radio = tk.Radiobutton(self.root, text="Female", variable=self.sex_var,  value="Female",font=self.font_style, bg=self.bg_color,fg=self.fg_color)
        self.female_radio.grid(row=8, column=1, padx=10, pady=5, sticky="e")

        # Department
        self.department_label = tk.Label(self.root,text="Department:",font=self.font_style, bg=self.bg_color, fg=self.fg_color)
        self.department_label.grid(row=9, column=0, padx=10, pady=5, sticky="e")
        self.department_entry = tk.Entry(self.root,font=self.font_style,width=25, bg=self.fg_color, fg="#2c3e50", relief=tk.FLAT )
        self.department_entry.grid(row=9, column=1, padx=10, pady=5)

        # Year
        self.year_label = tk.Label(self.root,text="Year:",font=self.font_style, bg=self.bg_color,fg=self.fg_color )
        self.year_label.grid(row=10, column=0, padx=10, pady=5, sticky="e")
        self.year_spinbox = tk.Spinbox( self.root, from_=1,to=8,font=self.font_style,bg=self.fg_color,fg="#2c3e50", relief=tk.FLAT)
        self.year_spinbox.grid(row=10, column=1, padx=10, pady=5)

        # Semester
        self.semester_label = tk.Label(self.root,text="Semester:",font=self.font_style, bg=self.bg_color,fg=self.fg_color)
        self.semester_label.grid(row=11, column=0, padx=10, pady=5, sticky="e")
        self.semester_spinbox = tk.Spinbox(self.root, from_=1,to=2,font=self.font_style, bg=self.fg_color,fg="#2c3e50",relief=tk.FLAT )
        self.semester_spinbox.grid(row=11, column=1, padx=10, pady=5)

        # Button Frame
        self.button_frame = tk.Frame(self.root, bg=self.bg_color)
        self.button_frame.grid(row=12, column=0, columnspan=2, pady=10)

        #  register Buttons
        self.register_button = tk.Button(self.button_frame,text="Register", font=self.font_style, bg=self.button_bg, fg=self.button_fg,relief=tk.FLAT,padx=10,pady=5,
            command=self.register_student )
        self.register_button.grid(row=0, column=0, padx=5)
        #clear btn

        self.clear_button = tk.Button(self.button_frame,text="Clear",font=self.font_style,bg="#e74c3c",  fg=self.button_fg, relief=tk.FLAT, padx=10, pady=5,
            command=self.clear_fields)
        self.clear_button.grid(row=0, column=1, padx=5)
        # back  btn
        self.back_button = tk.Button( self.button_frame, text="Back", font=self.font_style, bg="#95a5a6",  fg=self.button_fg,relief=tk.FLAT, padx=10, pady=5,
            command=self.go_back)
        self.back_button.grid(row=0, column=2, padx=5)
        

        


#---------------------------------------------------------------- register student method  ----------------

    def register_student(self):
        try:
            student_id = self.student_id_entry.get()
            username = self.username_entry.get()
            password = self.password_entry.get()
            email = self.email_entry.get()
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            age = self.age_spinbox.get()
            sex = self.sex_var.get()
            department = self.department_entry.get()
            year = self.year_spinbox.get()
            semester = self.semester_spinbox.get()

            if not all([student_id, username, password, email, first_name, last_name, age, sex, department, year, semester]):
                raise ValueError("All fields are required!")

            query = """
                INSERT INTO student (student_id, username, password, email, first_name, last_name, age, sex, department, year, semester)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            params = (student_id, username, password, email, first_name, last_name, age, sex, department, year, semester)
            cursor = execute_query(self.conn, query, params)
            if cursor:
                messagebox.showinfo("Success", "Student registered successfully!")
                self.clear_fields()
            else:
                messagebox.showerror("Error", "Failed to register student.")
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

#----------------------------------------------------------------clear_fields---------------------------------------------------------------- 
    def clear_fields(self):
        self.student_id_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.age_spinbox.delete(0, tk.END)
        self.sex_var.set("Male")  # Reset sex to default
        self.department_entry.delete(0, tk.END)
        self.year_spinbox.delete(0, tk.END)
        self.semester_spinbox.delete(0, tk.END)

#---------------------------------------------------------------- go back----------------------
    def go_back(self):
        self.root.destroy()
        self.main_app.root.deiconify()  # Show the main window




#================================================================ admin regestrations  class==============================
class AdminRegistrationForm:
    def __init__(self, root, main_app, conn):  # FIX: Added third parameter
        self.root = root
        self.main_app = main_app
        self.conn = conn
        self.root.title("Admin Registration")
        self.root.geometry("500x600")
       
        # Custom colors and fonts
        self.bg_color = "#2c3e50"  # Dark blue
        self.fg_color = "#ecf0f1"  # Light gray
        self.button_bg = "#3498db"  # Blue
        self.button_fg = "#ffffff"  # White
        self.font_style = ("Helvetica", 12)
        self.title_font = ("Helvetica", 16, "bold")
        
        # Set background color
        self.root.configure(bg=self.bg_color)
        self.create_widgets()
    #------------------widages ----------------------------------------------
    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Admin Registration", font=self.title_font,  bg=self.bg_color, fg=self.fg_color)
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # Admin ID
        self.admin_id_label = tk.Label(self.root,  text="Admin ID:", font=self.font_style, bg=self.bg_color,  fg=self.fg_color)
        self.admin_id_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.admin_id_entry = tk.Entry(self.root, font=self.font_style,  width=25, bg=self.fg_color, fg="#2c3e50",  relief=tk.FLAT)
        self.admin_id_entry.grid(row=1, column=1, padx=10, pady=5)

        # Username
        self.username_label = tk.Label(self.root, text="Username:", font=self.font_style,  bg=self.bg_color, fg=self.fg_color)
        self.username_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = tk.Entry( self.root, font=self.font_style,  width=25,  bg=self.fg_color, fg="#2c3e50", relief=tk.FLAT )
        self.username_entry.grid(row=2, column=1, padx=10, pady=5)

        # Password
        self.password_label = tk.Label(self.root, text="Password:",  font=self.font_style,  bg=self.bg_color, fg=self.fg_color)
        self.password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.root, font=self.font_style, width=25, show="*", bg=self.fg_color, fg="#2c3e50", relief=tk.FLAT)
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        # Email
        self.email_label = tk.Label( self.root, text="Email:", font=self.font_style,  bg=self.bg_color,  fg=self.fg_color)
        self.email_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry( self.root, font=self.font_style, width=25, bg=self.fg_color, fg="#2c3e50", relief=tk.FLAT)
        self.email_entry.grid(row=4, column=1, padx=10, pady=5)

        # First Name
        self.first_name_label = tk.Label(self.root, text="First Name:", font=self.font_style, bg=self.bg_color,  fg=self.fg_color)
        self.first_name_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.first_name_entry = tk.Entry(self.root, font=self.font_style, width=25, bg=self.fg_color,  fg="#2c3e50",  relief=tk.FLAT)
        self.first_name_entry.grid(row=5, column=1, padx=10, pady=5)

        # Last Name
        self.last_name_label = tk.Label(self.root,text="Last Name:", font=self.font_style, bg=self.bg_color, fg=self.fg_color)
        self.last_name_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.last_name_entry = tk.Entry(self.root,font=self.font_style, width=25, bg=self.fg_color, fg="#2c3e50", relief=tk.FLAT)
        self.last_name_entry.grid(row=6, column=1, padx=10, pady=5)

        # Age (Spinbox)
        self.age_label = tk.Label(self.root,text="Age:",  font=self.font_style,  bg=self.bg_color, fg=self.fg_color)
        self.age_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.age_spinbox = tk.Spinbox(self.root,  from_=1,  to=100, font=self.font_style, bg=self.fg_color, fg="#2c3e50",  relief=tk.FLAT)
        self.age_spinbox.grid(row=7, column=1, padx=10, pady=5)

        # Sex (Radio Buttons)
        self.sex_label = tk.Label(self.root,  text="Sex:", font=self.font_style,  bg=self.bg_color,fg=self.fg_color )
        self.sex_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.sex_var = tk.StringVar(value="Male")
        self.male_radio = tk.Radiobutton( self.root, text="Male",  variable=self.sex_var,  value="Male", font=self.font_style, bg=self.bg_color,  fg=self.fg_color)
        self.male_radio.grid(row=8, column=1, padx=10, pady=5, sticky="w")
        self.female_radio = tk.Radiobutton(self.root, text="Female", variable=self.sex_var,  value="Female", font=self.font_style,  bg=self.bg_color,fg=self.fg_color
        )
        self.female_radio.grid(row=8, column=1, padx=10, pady=5, sticky="e")

        # Position
        self.position_label = tk.Label(self.root, text="Position:", font=self.font_style, bg=self.bg_color,  fg=self.fg_color)
        self.position_label.grid(row=9, column=0, padx=10, pady=5, sticky="e")
        self.position_entry = tk.Entry(self.root, font=self.font_style,  width=25,  bg=self.fg_color,  fg="#2c3e50", relief=tk.FLAT)
        self.position_entry.grid(row=9, column=1, padx=10, pady=5)

        # Button Frame
        self.button_frame = tk.Frame(self.root, bg=self.bg_color)
        self.button_frame.grid(row=10, column=0, columnspan=2, pady=10)

        # Buttons
        self.register_button = tk.Button(self.button_frame, text="Register", font=self.font_style,  bg=self.button_bg,  fg=self.button_fg,  relief=tk.FLAT, padx=10, pady=5, 
            command=self.register_admin)
        self.register_button.grid(row=0, column=0, padx=5)
        self.clear_button = tk.Button( self.button_frame,  text="Clear", font=self.font_style, bg="#e74c3c",  fg=self.button_fg, relief=tk.FLAT, padx=10, pady=5, 
            command=self.clear_fields)
        self.clear_button.grid(row=0, column=1, padx=5)
        self.back_button = tk.Button(self.button_frame, text="Back",  font=self.font_style, bg="#95a5a6",  fg=self.button_fg,  relief=tk.FLAT, padx=10,pady=5, 
            command=self.go_back)
        self.back_button.grid(row=0, column=2, padx=5)

        
#----------regitration admin methode------------------------------------------------------
    def register_admin(self):
        try:
            admin_id = self.admin_id_entry.get()
            username = self.username_entry.get()
            password = self.password_entry.get()
            email = self.email_entry.get()
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            age = self.age_spinbox.get()
            sex = self.sex_var.get()
            position = self.position_entry.get()
            """
            save the admin data to the admin database table
            """
            if not all([admin_id, username, password, email, first_name, last_name, age, sex, position]):
                raise ValueError("All fields are required!")

            query = """
                INSERT INTO admin (admin_id, username, password, email, first_name, last_name, age, sex, position)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            params = (admin_id, username, password, email, first_name, last_name, age, sex, position)
            cursor = execute_query(self.conn, query, params)
            if cursor:
                messagebox.showinfo("Success", "Admin registered successfully!")
                self.clear_fields()
            else:
                messagebox.showerror("Error", "Failed to register admin.")
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")


    #-----------------------------------clear the admin data-----------------------------        
    def clear_fields(self):
        self.admin_id_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.age_spinbox.delete(0, tk.END)
        self.sex_var.set("Male")
        self.position_entry.delete(0, tk.END)
    #------------------------------------go back to the main window-----------------------------
    def go_back(self):
        self.root.destroy()
        self.main_app.root.deiconify()  # Show the main window

#**********************Student Dashbord Class*******************************************==========================================================================================================================--------------------------------------------------------------------------------------------------------------
class StudentDashboard:
    def __init__(self, root, student_id, conn, first_name):
        self.root = root
        self.student_id = student_id
        self.conn = conn
        self.root.title(f"Student Dashboard - {first_name}")
        self.root.geometry("1200x800")
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('Treeview', rowheight=25)
        
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Left navigation panel
        nav_frame = ttk.Frame(main_frame, width=200, style='Nav.TFrame')
        nav_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Buttons with styling
        btn_style = {'style': 'TButton', 'width': 15}
        ttk.Button(nav_frame, text="Submit Complaint", 
                  command=self.show_submit_form, **btn_style).pack(pady=10)
        ttk.Button(nav_frame, text="View Complaints", 
                  command=self.load_complaints, **btn_style).pack(pady=10)
        ttk.Button(nav_frame, text="Log Out", 
                  command=self.logout, **btn_style).pack(pady=10)

        # Complaint list treeview
        self.tree = ttk.Treeview(main_frame, columns=(
            'ID', 'Title', 'Category', 'Status', 'Date', 'Priority', 'Resolution'
        ), show='headings')
        
        # Configure columns
        columns = [
            ('ID', 'Complaint ID', 100),
            ('Title', 'Title', 100),
            ('Category', 'Category', 100),
            ('Status', 'Status', 100),
            ('Date', 'Submission Date', 150),
            ('Priority', 'Priority', 100),
            ('Resolution', 'Resolution', 150)
        ]
        
        for col, heading, width in columns:
            self.tree.heading(col, text=heading)
            self.tree.column(col, width=width, anchor=tk.W)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Load initial complaints
        self.load_complaints()
    #-----------------Loading complaint-----------------------------------------------
    # In StudentDashboard's load_complaints method
    def load_complaints(self):
        self.tree.delete(*self.tree.get_children())
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT complaint_id, title, category, status,
                    submission_date, priority, resolution_details
                FROM Complaints
                WHERE student_id = ?
            """, (self.student_id,))
            
            for row in cursor.fetchall():
                # Convert numeric priority to text
                priority_map = {1: 'High', 2: 'Medium', 3: 'Low'}
                formatted_row = list(row)
                formatted_row[5] = priority_map.get(formatted_row[5], 'Unknown')
                
                # Convert None resolution to empty string
                formatted_row[6] = formatted_row[6] or ''
                
                # Format datetime
                formatted_row[4] = row[4].strftime("%Y-%m-%d %H:%M")
                
                self.tree.insert('', tk.END, values=formatted_row)
                
            cursor.close()
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Failed to load complaints: {str(e)}")
#-----------show submit rm methodes-----------------------------------------------------

    def show_submit_form(self):
        # Create submission window
        self.submit_window = tk.Toplevel(self.root)
        self.submit_window.title("Submit New Complaint")
        self.submit_window.geometry("600x400")
        self.submit_window.configure(bg="#4287f5")

        # Form frame
        form_frame = ttk.Frame(self.submit_window)
        form_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Form elements
        ttk.Label(form_frame, text="Title:", font=('Helvetica', 12)).grid(row=0, column=0, sticky='w', pady=5)
        self.title_entry = ttk.Entry(form_frame, width=50)
        self.title_entry.grid(row=0, column=1, pady=5, padx=10)

        ttk.Label(form_frame, text="Category:", font=('Helvetica', 12)).grid(row=1, column=0, sticky='w', pady=5)
        self.category_combo = ttk.Combobox(form_frame, values=[
            'Academic', 'Hostel', 'Financial', 'Infrastructure',
            'Faculty', 'Administrative', 'Other'
        ], state='readonly')
        self.category_combo.grid(row=1, column=1, pady=5, padx=10)

        ttk.Label(form_frame, text="Description:", font=('Helvetica', 12)).grid(row=2, column=0, sticky='nw', pady=5)
        self.desc_text = scrolledtext.ScrolledText(form_frame, width=50, height=10, wrap=tk.WORD)
        self.desc_text.grid(row=2, column=1, pady=5, padx=10)

        # Submit button
        submit_btn = ttk.Button(form_frame, text="Submit Complaint", 
                              command=self.save_complaint,
                              style="Submit.TButton")
        submit_btn.grid(row=3, column=1, pady=15, sticky='e')
    #-----------------save complaint to complaint table-----------------------------------------------------
    def save_complaint(self):
        # Get form data
        title = self.title_entry.get().strip()
        category = self.category_combo.get()
        description = self.desc_text.get("1.0", tk.END).strip()

        # Validate inputs
        if not title or not category or not description:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO Complaints (
                    student_id, title, description, category,
                    submission_date, status, priority
                ) VALUES (?, ?, ?, ?, GETDATE(), 'Open', 3)
            """, (self.student_id, title, description, category))
            
            self.conn.commit()
            messagebox.showinfo("Success", "Complaint submitted successfully!")
            self.submit_window.destroy()
            self.load_complaints()  # Refresh the list
            
        except pyodbc.Error as e:
            messagebox.showerror("Database Error", f"Failed to submit complaint: {str(e)}")
        finally:
            cursor.close()

#-----------------logout method that redirects to the login page -----------------------------------------------------
    def logout(self):
        self.root.destroy()
        login_root = tk.Tk()
        ComplaintManagementApp(login_root)
        login_root.mainloop()
   


#--***Admin dashbord************************************************************************************-------------------------------------------------------------------------------
class AdminDashboard:
    def __init__(self, root, admin_id, conn, first_name):
        
        self.root = root
        self.admin_id = admin_id
        self.conn = conn
        self.root.title(f"Admin Dashboard - {first_name}")
        self.root.geometry("1400x800")
        
        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('Treeview', rowheight=25, font=('Helvetica', 11))
        self.style.configure('Header.Treeview', font=('Helvetica', 12, 'bold'))
        
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Left navigation panel
        nav_frame = ttk.Frame(main_frame, width=220, style='Nav.TFrame')
        nav_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Admin-specific buttons
        btn_style = {'style': 'TButton', 'width': 18}
        ttk.Button(nav_frame, text="View All Complaints", 
                  command=self.load_all_complaints, **btn_style).pack(pady=12)
        ttk.Button(nav_frame, text="Resolve Complaint", 
                  command=self.resolve_complaint, **btn_style).pack(pady=12)
        ttk.Button(nav_frame, text="Generate Report", 
                  command=self.generate_report, **btn_style).pack(pady=12)
        ttk.Button(nav_frame, text="Manage Complaints", 
                  command=self.manage_complaints, **btn_style).pack(pady=12)
        ttk.Button(nav_frame, text="Log Out", 
                  command=self.logout, **btn_style).pack(pady=12)


        # Complaints Treeview
        self.tree = ttk.Treeview(main_frame, columns=(
            'ID', 'Title', 'Category', 'Status', 'Date', 'Student', 'Priority', 'Resolution'
        ), show='headings')
        
        # Configure columns
        columns = [
            ('ID', 'Complaint ID', 50),
            ('Title', 'Title', 150),
            ('Category', 'Category', 100),
            ('Status', 'Status', 100),
            ('Date', 'Submission Date', 150),
            ('Student', 'Student ID', 80),
            ('Priority', 'Priority', 45),
            ('Resolution', 'Resolution', 200)
        ]
        
        for col, heading, width in columns:
            self.tree.heading(col, text=heading)
            self.tree.column(col, width=width, anchor=tk.W)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Load initial complaints
        self.load_all_complaints()


    #---loading complaints to admin dashbord-------------------------------------------------------------
    # In AdminDashboard's load_all_complaints method
    def load_all_complaints(self):
        self.tree.delete(*self.tree.get_children())
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT complaint_id, title, category, status,
                    submission_date, student_id, priority, resolution_details
                FROM Complaints
            """)
            
            for row in cursor.fetchall():
                # Convert numeric priority to text
                priority_map = {1: 'High', 2: 'Medium', 3: 'Low'}
                formatted_row = list(row)
                formatted_row[6] = priority_map.get(formatted_row[6], 'Unknown')
                
                # Convert None resolution to empty string
                formatted_row[7] = formatted_row[7] or ''
                
                # Format datetime
                formatted_row[4] = row[4].strftime("%Y-%m-%d %H:%M")
                
                self.tree.insert('', tk.END, values=formatted_row)
                
            cursor.close()
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Failed to load complaints: {str(e)}")  
#---resolve complaint---------------------------------------------------------------------------------------            
    def resolve_complaint(self):
        self.resolve_window = tk.Toplevel(self.root)
        self.resolve_window.title("Resolve Complaint")
        self.resolve_window.geometry("500x400")
        self.resolve_window.configure(bg="#f0f2f5")

        # Form frame
        form_frame = ttk.Frame(self.resolve_window)
        form_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Complaint ID
        ttk.Label(form_frame, text="Complaint ID:", font=('Helvetica', 12)).grid(row=0, column=0, sticky='w', pady=5)
        self.complaint_id_entry = ttk.Entry(form_frame, width=15)
        self.complaint_id_entry.grid(row=0, column=1, pady=5, padx=10, sticky='w')

        # Resolution Status
        ttk.Label(form_frame, text="Resolution Status:", font=('Helvetica', 12)).grid(row=1, column=0, sticky='w', pady=5)
        self.status_combo = ttk.Combobox(form_frame, values=[
            'Resolved', 'Closed', 'Rejected'
        ], state='readonly')
        self.status_combo.grid(row=1, column=1, pady=5, padx=10, sticky='w')

        # Resolution Details
        ttk.Label(form_frame, text="Resolution Details:", font=('Helvetica', 12)).grid(row=2, column=0, sticky='nw', pady=5)
        self.resolution_text = scrolledtext.ScrolledText(form_frame, width=40, height=8, wrap=tk.WORD)
        self.resolution_text.grid(row=2, column=1, pady=5, padx=10)

        # Resolve Button
        resolve_btn = ttk.Button(form_frame, text="Submit Resolution", 
                               command=self.submit_resolution,
                               style="Resolve.TButton")
        resolve_btn.grid(row=3, column=1, pady=15, sticky='e')
#---submit resolved complaint button-------------------------------------------------------------
    def submit_resolution(self):
        # Get form data
        complaint_id = self.complaint_id_entry.get().strip()
        status = self.status_combo.get()
        resolution = self.resolution_text.get("1.0", tk.END).strip()

        # Validate inputs
        if not complaint_id or not status or not resolution:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            # Check if complaint exists
            cursor = self.conn.cursor()
            cursor.execute("SELECT complaint_id FROM Complaints WHERE complaint_id = ?", (complaint_id,))
            if not cursor.fetchone():
                messagebox.showerror("Error", "Invalid Complaint ID!")
                return

            # Update complaint
            cursor.execute("""
                UPDATE Complaints 
                SET resolution_details = ?,
                    status = ?,
                    resolution_date = GETDATE(),
                    admin_id = ?
                WHERE complaint_id = ?
            """, (resolution, status, self.admin_id, complaint_id))
            
            self.conn.commit()
            messagebox.showinfo("Success", "Complaint resolved successfully!")
            self.resolve_window.destroy()
            self.load_all_complaints()  # Refresh the list
            
        except pyodbc.Error as e:
            messagebox.showerror("Database Error", f"Failed to resolve complaint: {str(e)}")
        finally:
            cursor.close()

#---Report genratores methode-------------------------------------------------------------     
    def generate_report(self):
        """Generate and display a report of complaint statistics"""
        # Create report window
        report_window = tk.Toplevel(self.root)
        report_window.title("Complaint Statistics Report")
        report_window.geometry("800x600")
        report_window.configure(bg="#4287f5")

        # Main container
        main_frame = ttk.Frame(report_window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title
        ttk.Label(main_frame, 
                text="Complaint Statistics Report", 
                font=('Helvetica', 16, 'bold')).pack(pady=15)

        try:
            cursor = self.conn.cursor()
            
            # Get status distribution
            cursor.execute("""
                SELECT status, COUNT(*) AS count 
                FROM Complaints 
                GROUP BY status
            """)
            status_data = cursor.fetchall()
            status_dict = {status: count for status, count in status_data}

            # Get total complaints
            cursor.execute("SELECT COUNT(*) FROM Complaints")
            total_complaints = cursor.fetchone()[0]

            # Get category distribution
            cursor.execute("""
                SELECT category, COUNT(*) AS count 
                FROM Complaints 
                GROUP BY category
            """)
            category_data = cursor.fetchall()

            # Get priority distribution
            cursor.execute("""
                SELECT priority, COUNT(*) AS count 
                FROM Complaints 
                GROUP BY priority
            """)
            priority_data = cursor.fetchall()

            cursor.close()

        except pyodbc.Error as e:
            messagebox.showerror("Database Error", f"Failed to generate report: {str(e)}")
            return

        # Status Statistics Frame
        status_frame = ttk.LabelFrame(main_frame, text="Status Distribution")
        # status_frame.config(bg="#4287f5")
        status_frame.pack(fill=tk.X, pady=10, padx=10)

        predefined_statuses = ['Open', 'In Progress', 'Resolved', 'Closed', 'Rejected']
        for status in predefined_statuses:
            row = ttk.Frame(status_frame)
            row.pack(fill=tk.X, pady=3)
            ttk.Label(row, text=status, width=15, anchor='w').pack(side=tk.LEFT, padx=5)
            ttk.Label(row, text=str(status_dict.get(status, 0))).pack(side=tk.RIGHT, padx=5)

        # Total Complaints
        total_frame = ttk.LabelFrame(main_frame, text="Total Complaints")
        total_frame.pack(fill=tk.X, pady=10, padx=10)
        ttk.Label(total_frame, text=str(total_complaints), font=('Helvetica', 14)).pack(pady=5)

        # Category Statistics Frame
        category_frame = ttk.LabelFrame(main_frame, text="Category Distribution")
        category_frame.pack(fill=tk.BOTH, pady=10, padx=10, expand=True)

        for category, count in category_data:
            row = ttk.Frame(category_frame)
            row.pack(fill=tk.X, pady=3)
            ttk.Label(row, text=category, width=20, anchor='w').pack(side=tk.LEFT, padx=5)
            ttk.Label(row, text=str(count)).pack(side=tk.RIGHT, padx=5)

        # Priority Statistics Frame
        priority_frame = ttk.LabelFrame(main_frame, text="Priority Distribution")
        priority_frame.pack(fill=tk.BOTH, pady=10, padx=10, expand=True)


        for priority, count in priority_data:
            row = ttk.Frame(priority_frame)
            row.pack(fill=tk.X, pady=3)
            ttk.Label(row, text=priority, width=15, anchor='w').pack(side=tk.LEFT, padx=5)
            ttk.Label(row, text=str(count)).pack(side=tk.RIGHT, padx=5)


        # Add disclaimer about deleted/updated tracking
        disclaimer = ttk.Label(main_frame, 
                            text="Note: Historical tracking of deletions and updates requires additional logging.", 
                            font=('Helvetica', 9), 
                            foreground='gray50')
        disclaimer.pack(pady=10)

            # Implementation for report generation


    def manage_complaints(self):
        # Create management window
        self.manage_window = tk.Toplevel(self.root)
        self.manage_window.title("Manage Complaints")
        self.manage_window.geometry("400x250")
        self.manage_window.configure(bg="#4287f5")

        # Form frame
        form_frame = ttk.Frame(self.manage_window)
        form_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Complaint ID
        ttk.Label(form_frame, text="Complaint ID:", font=('Helvetica', 12)).grid(row=0, column=0, sticky='w', pady=10)
        self.manage_complaint_id = ttk.Entry(form_frame, width=15)
        self.manage_complaint_id.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        # Delete Button
        delete_btn = ttk.Button(form_frame, text="Delete Complaint", 
                              command=self.delete_complaint,
                              style="Danger.TButton")
        delete_btn.grid(row=1, column=1, pady=15, sticky='e')
        # Update Button
        update_btn = ttk.Button(form_frame, text="Update Complaint", 
                              command=self.update_complaint,
                              style="Update.TButton")
        update_btn.grid(row=1, column=0, pady=15, sticky='e')


    def delete_complaint(self):
        complaint_id = self.manage_complaint_id.get().strip()
        
        if not complaint_id:
            messagebox.showerror("Error", "Please enter a Complaint ID!")
            return

        confirm = messagebox.askyesno("Confirm Delete", 
                                    "Are you sure you want to delete this complaint?\nThis action cannot be undone!")
        if not confirm:
            return

        try:
            cursor = self.conn.cursor()
            
            # Check if complaint exists
            cursor.execute("SELECT complaint_id FROM Complaints WHERE complaint_id = ?", (complaint_id,))
            if not cursor.fetchone():
                messagebox.showerror("Error", "Invalid Complaint ID!")
                return

            # Delete complaint
            cursor.execute("DELETE FROM Complaints WHERE complaint_id = ?", (complaint_id,))
            self.conn.commit()
            
            messagebox.showinfo("Success", "Complaint deleted successfully!")
            self.manage_window.destroy()
            self.load_all_complaints()  # Refresh the list
            
        except pyodbc.Error as e:
            messagebox.showerror("Database Error", f"Failed to delete complaint: {str(e)}")
        finally:
            cursor.close()

   


    def update_complaint(self):
        # Create update window
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title("Update Complaint Details")
        self.update_window.geometry("500x400")
        self.update_window.configure(bg="#4287f5")

        # Form frame
        form_frame = ttk.Frame(self.update_window)
        form_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Complaint ID
        ttk.Label(form_frame, text="Complaint ID:", font=('Helvetica', 12)).grid(row=0, column=0, sticky='w', pady=5)
        self.update_id_entry = ttk.Entry(form_frame, width=15)
        self.update_id_entry.grid(row=0, column=1, pady=5, padx=10, sticky='w')

        # Category Update
        ttk.Label(form_frame, text="New Category:", font=('Helvetica', 12)).grid(row=1, column=0, sticky='w', pady=5)
        self.new_category = ttk.Combobox(form_frame, values=[
            'Academic', 'Hostel', 'Financial', 'Infrastructure',
            'Faculty', 'Administrative', 'Other'
        ], state='readonly')
        self.new_category.grid(row=1, column=1, pady=5, padx=10, sticky='w')

        # Status Update
        ttk.Label(form_frame, text="New Status:", font=('Helvetica', 12)).grid(row=2, column=0, sticky='w', pady=5)
        self.new_status = ttk.Combobox(form_frame, values=[
            'Open', 'In Progress', 'Resolved', 'Closed', 'Rejected'
        ], state='readonly')
        self.new_status.grid(row=2, column=1, pady=5, padx=10, sticky='w')

        # Update Button
        update_btn = ttk.Button(form_frame, text="Update Complaint", 
                              command=self.submit_update,
                              style="Update.TButton")
        update_btn.grid(row=3, column=1, pady=15, sticky='e')

#----------------------------------------------------------------
    def submit_update(self):
    # Submit update request to the database
        complaint_id = self.update_id_entry.get().strip()
        new_category = self.new_category.get()
        new_status = self.new_status.get()

        if not complaint_id:
            messagebox.showerror("Error", "Complaint ID is required!")
            return

        try:
            cursor = self.conn.cursor()
            
            # Check if complaint exists
            cursor.execute("SELECT complaint_id FROM Complaints WHERE complaint_id = ?", (complaint_id,))
            if not cursor.fetchone():
                messagebox.showerror("Error", "Invalid Complaint ID!")
                return

            # Build update query
            update_fields = []
            params = []
            
            if new_category:
                update_fields.append("category = ?")
                params.append(new_category)
            if new_status:
                update_fields.append("status = ?")
                params.append(new_status)

            if not update_fields:
                messagebox.showerror("Error", "No fields to update!")
                return

            params.append(complaint_id)
            query = f"UPDATE Complaints SET {', '.join(update_fields)} WHERE complaint_id = ?"
            
            cursor.execute(query, params)
            self.conn.commit()
            
            messagebox.showinfo("Success", "Complaint updated successfully!")
            self.update_window.destroy()
            self.load_all_complaints()  # Refresh the list
            
        except pyodbc.Error as e:
            messagebox.showerror("Database Error", f"Failed to update complaint: {str(e)}")
        finally:
            cursor.close()

    def logout(self):
        #-------return to main window----------------------------------------------------------------
        self.root.destroy()
        login_root = tk.Tk()
        ComplaintManagementApp(login_root)
        login_root.mainloop()
   



if __name__ == "__main__":
    root = tk.Tk()
    app = ComplaintManagementApp(root)
    root.mainloop()
"""
create database STMS;
USE STMS;

CREATE TABLE student (
    student_id VARCHAR(20) PRIMARY KEY,  -- Unique ID for each student
    username VARCHAR(50) NOT NULL UNIQUE,  -- Username for login
    password VARCHAR(100) NOT NULL,  -- Password for login
    email VARCHAR(100) NOT NULL UNIQUE,  -- Email address
    first_name VARCHAR(50) NOT NULL,  -- First name
    last_name VARCHAR(50) NOT NULL,  -- Last name
    age INT NOT NULL,  -- Age of the student
    sex VARCHAR(10) NOT NULL,  -- Sex (Male/Female)
    department VARCHAR(100) NOT NULL,  -- Department (e.g., Computer Science)
    year INT NOT NULL,  -- Year of study (1, 2, 3, 4)
    semester INT NOT NULL  -- Semester (1 or 2)
);
select *from student



CREATE TABLE admin (
    admin_id VARCHAR(20) PRIMARY KEY,  -- Unique ID for each admin
    username VARCHAR(50) NOT NULL UNIQUE,  -- Username for login
    password VARCHAR(100) NOT NULL,  -- Password for login
    email VARCHAR(100) NOT NULL UNIQUE,  -- Email address
    first_name VARCHAR(50) NOT NULL,  -- First name
    last_name VARCHAR(50) NOT NULL,  -- Last name
    age INT NOT NULL,  -- Age of the admin
    sex VARCHAR(10) NOT NULL,  -- Sex (Male/Female)
    position VARCHAR(100) NOT NULL  -- Position (e.g., System Administrator)
);


select  * from admin;



CREATE TABLE Complaints (
    complaint_id INT PRIMARY KEY IDENTITY(1,1),
    student_id VARCHAR(20) NOT NULL,
    admin_id VARCHAR(20) NULL,
    title NVARCHAR(100) NOT NULL,
    description NVARCHAR(MAX) NOT NULL,
    category NVARCHAR(50) NOT NULL CHECK (category IN (
        'Academic', 'Hostel', 'Financial', 'Infrastructure', 
        'Faculty', 'Administrative', 'Other'
    )),
    status NVARCHAR(20) NOT NULL DEFAULT 'Open' CHECK (status IN (
        'Open', 'In Progress', 'Resolved', 'Closed', 'Rejected'
    )),
    submission_date DATETIME NOT NULL DEFAULT GETDATE(),
    assigned_date DATETIME NULL,
    resolution_details NVARCHAR(MAX) NULL,
    resolution_date DATETIME NULL,
    priority INT DEFAULT 3 CHECK (priority BETWEEN 1 AND 3),
    
    -- Foreign key constraints
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE NO ACTION,
    FOREIGN KEY (admin_id) REFERENCES admin(admin_id) ON DELETE SET NULL
);




 select * from  Complaints"""
