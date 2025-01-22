
lists_month=["Sebtember","October","November","December","January","Feburary","March","April","May","June","July","Agust"]
print(lists_month)
month=input("enter the month of year from the above lists of month").strip().capitalize()    

match month:
    case "September":
        print(f"the season is Automun")
    case "October":
        print(f"the season is Automun")
    case "November":
        print(f"the season is Automun")
    case "December":
        print("The season is winter")
    case "January":
        print("The season is winter")
    case "Feburary":
        print("The season is winter")
    case "April":
        print("The season is spring")         
    case "Murch":
        print("The season is spring")    
    case "May":
        print("The season is spring")
    case "Jun":
        print("The season is summery")           
    case "July":
        print("The season is summery")
    case "Augest":
        print("The season is summery")
    case _:
        print("invalid input")        
       
