#Data Storage (text file)
STUDENTS_FILE="Students.txt"
COURSES_FILE="Courses.txt"
ENROLLMENTS="Enrollments.txt"
RESULTS="Results.txt"

Maximum_Courses=3

#GPA
GPA={"A+":4.00,"A":3.70,"B+":3.30,"B":3.00,"C+":2.70,"C":2.30,"D+":1.70,"D":1.30,"F":1.00,"F-":0.00}

#Register Course
def register_courses(students_id):
    print("\n-----Register Courses-----")
    courses={}
    with open("Courses.txt","r") as f:
        for line in f:
            parts=line.strip().split(",")
            if len(parts)==3:
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

##check if the student registered for more than 3 course
if len(my_courses)>=Maximum_Courses:
    print(f"You have already registered {Maximum_Courses} courses")
