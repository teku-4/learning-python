#chek days of weeek
day=input("enter the day").strip().lower()
match day:
    case "monday":
        print(f"the day today is monday")
    case "tuesday":
        print(f"the day today is tuesday")
    case "wednesday":
        print(f"the day today is wednsday")
    case "thrusday":
        print(f"the day today is thrusday")
    case "friday":
        print(f"the day today is friday")
    case "saturday":
        print(f"the day today is saturday")
    case "sunday":
        print(f"the day today is sunday")
    case _:
        print("wrong input")                        
