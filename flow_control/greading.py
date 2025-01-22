mark=float(input("Enter the mark of students:\n"))
if mark>=0 and mark<=100:
    if mark>=90:
        print("grade is A+")
    elif mark >=85:
        print("grade is A")
    elif mark>=80:
        print("the grade is A-")
    elif mark>=75:
        print("the grade is B+")
    elif mark>=70:
        print("the garde is B") 
    elif mark>=65:
        print("the grade is B-")
    elif mark>=60:
        print("the grade is C+")
    elif mark>=55:
        print("the grade is C")
    elif mark >=50:
        print("the grade C-")
    elif mark>=45:
        print("the grade is D")
    else:
        print("the grade is F")
else:
    print("please the valid input:")