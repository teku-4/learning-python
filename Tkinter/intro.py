from tkinter import *
# root=Tk()
# root.title("tkinter GUI")
# root.geometry("200x200")
# fristPractice=Label(root,text="hellow world")
# fristPractice.pack()
# fristPractice.mainloop()
# #button usage
# import tkinter as tk

# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()
# #entry usage
# master=Tk()
# Label(master,text='Frist Name:').grid(row=0)
# Label(master,text='Last Name: ').grid(row=1)
# entry1=Entry(master)
# entry2=Entry(master)
# entry1.grid(row=0,column=1)

# entry2.grid(row=1,column=1)

# mainloop()
#usage of check button
# master=Tk()
# var1=IntVar()
# Checkbutton(master,text="Male ",
#             variable=var1).grid(row=0,sticky=W)
# var1=IntVar()
# Checkbutton(master,text="Female ",
#             variable=var1).grid(row=1,sticky=W)
# mainloop()
# #usage of radio button
# master=Tk()
# master.title("radiocheck boxe")
# master.geometry("400x6")
# var=IntVar()
# Radiobutton(master,text="male",variable=var,value=1).pack(anchor=W)
# Radiobutton(master,text="female",variable=var,value=2).pack(anchor=W)
# mainloop()


top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop()
