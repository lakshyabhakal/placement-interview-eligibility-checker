def info():
    print("Welcome, future CS engineers!.\n")
      
    print("Disclaimer : This is only for final year students.\n")

    print("Are you excited to check your interview eligibility?\n" )

def userinput():
    while True:
        Name = input("Enter first name only:").strip()
        if Name.isalpha():
            print(f"Thank you, {Name.title()}.")
            break
        else:
            print("Enter your correct name only.")
        

    while True:
        try:
            mark10 = float(input("Enter your class 10 percentage:"))
            if mark10 >= 0 and mark10 <= 100:
                print("Class 10 percentage :", mark10 )
                break
            else:
                print("Error, enter percentage between 0-100")
        except ValueError:
                print("Enter your marks only")
    while True:
        try:
            mark12 = float(input("Enter your class 12 percentage:"))
            if mark12 >= 0 and mark12 <= 100:
                print("Class 12 percentage :", mark12)
                break
            else:
                print("Error, enter percentage between 0-100")
        except ValueError:
            print("Enter your marks only")

    while True:
        try:
            Semester = int(input("Enter your current semester:"))
    
            if Semester == 7 or Semester == 8:
                print("Semester:", Semester)
                break
            else:
                print("Enter valid semester.")
        except ValueError:
            print("Enter correct semester (7-8)")

    while True:
        try:
            Backlog = int(input("Enter your active backlog:"))
            if Backlog >= 0 and Backlog <= 6:
                print("Active backlog:", Backlog)
                break
            else:
                print("Maximum backlogs you can have are 6.")
        except ValueError:
            print("Enter current backlog:")

    while True:
        try:
            cgpa = float(input("Enter your cumulative cgpa: "))  
            if cgpa >= 0 and cgpa <= 10:
                print("Your cgpa:", cgpa)
                break
            else:
                print("Enter, cgpa (0-10)")
        except ValueError:
            print("Enter, cgpa (0-10) only.")
    return Name,mark10,mark12,Semester,Backlog,cgpa


def evaluation(mark10, mark12, Backlog, cgpa):  
    if mark10 >= 60 and mark12 >= 60 and Backlog == 0 and cgpa >= 8.5:
        return True
    else:
        return False

info()
Name, mark10, mark12, Semester, Backlog, cgpa = userinput()
eligible = evaluation( mark10, mark12, Backlog, cgpa)

if eligible:
    print(f"\n{Name}, of semester {Semester}. Congratulations! You are eligible for placement interview.")
else:
    print(f"\n{Name}, of semester {Semester}. Sorry! but you are not eligible for placement interview.")