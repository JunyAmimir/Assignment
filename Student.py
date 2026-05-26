"""
Student
• Register Courses: Select and register available courses
• View Registered Courses: Display courses enrolled
• View Results: View grades and simple GPA calculation
"""


#Data Storage (text file)
STUDENTS_FILE="Students.txt"
COURSES_FILE="Courses.txt"
ENROLLMENTS="Enrollments.txt"
RESULTS="Results.txt"

Maximum_Courses=3

#GPA
GPA={"A+":4.00,"A":3.70,"B+":3.30,"B":3.00,"C+":2.70,"C":2.30,"D+":1.70,"D":1.30,"F":1.00,"F-":0.00}


#Student Login
def student_login():
    print("\n---Student Login---")
    student_id=input("Enter Student ID:").strip()
    password=input("Enter Password:").strip()

    try:
        with open("Students.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==3:
                    sid,pwd=parts
                    if sid.strip()==student_id and  pwd.strip()==password:
                        print(f"Welcome {student_id}")
                        return student_id
    except FileNotFoundError:
        print("Error:Students.txt not fount")
        return None
    print("Invalid Student id or Password.")
    return None

#Register Course.txt
def register_course(students_id):
    print("\n-----Register Courses-----")
    students_id=int(students_id)
    courses={}
    with open("Courses.txt","r") as f:
        for line in f:
            parts=line.strip().split(",")
            if len(parts)==2:
                courses[parts[0].strip()]=[parts[1].strip(),parts[2].strip()]
    print("Error:Courses.txt not fount")
    return
        
#students currents enrollments
my_courses={}
try:
    with open("Enrollments.txt","r") as f:
        for line in f:
            parts=line.strip().split(",")
            if len(parts)==2 and parts[0].strip()==STUDENTS_FILE:
                my_courses.append(parts[1])
except FileNotFoundError:
    pass

#check if the student registered for more than 3 course
if len(my_courses)>=Maximum_Courses:
    print(f"You have already registered {Maximum_Courses} courses")

#Show available course
print(f"\n{'code'}{'Course.txt Name'}")
for code,info in my_courses.items():
    tag="<enrollment>"if code in my_courses else""

    print(f"{'Code'}{'Info[0]'}")
choice=int(input("Enter Course.txt Code to Register(Press 0 to cancel):"))
if choice=="0":
    print("Cancelling...")

elif choice not in my_courses:
    print("Invalid Choice Please try again")

elif choice in my_courses:
    print("You are already registered in this course")

else:
    with open("Enrollments.txt","a") as f:
        f.write(f"{'students_id'},{'choice'}\n")
    print("Successfully registered:{courses[choice][0]}")

#View Register Courses
def view_registered_course():
    print("\n-----View Registered Courses-----")
    courses={}
    try:
        with open("Enrollments.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==2:
                    courses[parts[0].strip()]=[parts[1].strip(),parts[2].strip()]
    except FileNotFoundError:
        print("Error:Enrollments.txt not fount")
        return
    my_courses={}
    try:
        with open("Enrollments.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==2 and parts[0].strip()==STUDENTS_FILE:
                    my_courses[parts[0].strip()]=[parts[1].strip(),parts[2].strip()]
    except FileNotFoundError:
        pass

    if not my_courses:
        print("You have not registered any courses")
        return

    print(f"\n{'code'}{'Course.txt Name'}")
    total=0
    for i, code in enumerate(my_courses,1):
        if code in my_courses:
            print(f"{code},{my_courses[code]}")
        else:
            print(f"[Not Found]")
    print(f"Total Courses: {len(my_courses)}/{Maximum_Courses}")

#View GPA
def view_result(students_id):
    print("\n-----View My Results and GPA-----")
    courses={}
    try:
        with open("Courses.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==2:
                    courses[parts[0].strip()]=[parts[1].strip()]
    except FileNotFoundError:
        print("Error:Courses.txt not fount")
        return

    my_courses=[]
    try:
        with open("Enrollments.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==2 and parts[0].strip()==students_id:
                    my_courses.append(parts[1].strip())
    except FileNotFoundError:
        pass

    if not my_courses:
        print("You have not registered any courses")
        return

    my_grades=[]
    try:
        with open("Result.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==3 and parts[0].strip()==students_id:
                    my_grades[parts[1].strip()]=[parts[2].strip()]
    except FileNotFoundError:
        pass

    print(f"\n{'code'}{'Course.txt Name'}{'Grade'}")
    total_credits=0
    weighted_total=0.0

    for i, code in enumerate(my_courses,1):
        if code in courses:
            name=courses[code]
            grade=my_grades.get(code,"Pending")
            points=GPA.get(grade,"-")
            print(f"{code},{name},{grade},{points}")

            if grade in GPA:
                weighted_total += GPA[grade]
                total_credits += 1
    print("-"*60)
    if total_credits>0:
        gpa=weighted_total/total_credits
        print(f"Total GPA: {gpa}/4.00")
    else:
        print(f"No Grades Recorded")

