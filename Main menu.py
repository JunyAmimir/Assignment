def main_menu():
  while True:
#while True function used to infinite loop the main menu
    print("                                                              ")
    print("==============================================================")
    print("Administrator Login, type 1")
    print("Student Login, type 2")
    print("Exit, type 3")
    print("==============================================================")
    print("                                                              ")

    choice = int(input("Enter your choice: "))
    try:
        if choice==1:
            Admin_id=input("Enter your Admin ID: ")
            Admin_password=input("Enter your Admin Password: ")
            file=open('Admin.txt','r')
            correct=file.read().strip().split(',')
            file.close()
            if Admin_id==correct[0] and Admin_password==correct[1]:
                print("Login successful!")
                admin_menu()
            else:
                print("Invalid Admin ID or Password. Please try again.")
        elif choice==2:
            Student_id=input("Enter your Student ID: ")
            Student_password=input("Enter your Student Password: ")
            file=open('Student.txt','r')
            correct=file.read().strip().split(',')
            file.close()
            if Student_id==correct[0] and Student_password==correct[1]:
                print("Login successful!")
                student_menu(Student_id)
                break
            else:
                print("Invalid Student ID or Password. Please try again.")
        elif choice==3:
            print("Thank you for using the system. Closing the system....... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Error! Please enter a valid number!")

#Admin Main Menu function
def admin_menu():
    while True:
        print("Welcome,Admin")
        print("                                    ")
        print("====================================")
        print("Manage Students Record, type 1")
        print("Manage Course Information, type 2")
        print("View Enrolment Record, type 3")
        print("Generate Reports, type 4")
        print("Back to Main Menu, type 5")
        print("====================================")
        print("                                    ")

        choice=int(input("Enter your choice: "))
        if choice==1:
            student_record()
        elif choice==2:
            course_info()
        elif choice==3:
            view_enrollment()
        elif choice==4:
            generate()
        elif choice==5:
            print("Logging out... Redirect to Main Menu")
            break
        else:
            print("Invalid choice. Please try again.")

#Student Record Menu function
def student_record():
    while True:
        print("                                        ")
        print("========================================")
        print("Add Student Information, type 1")
        print("Update Student Information, type 2")
        print("Remove Student Information, type 3")
        print("Back to Admin Menu, type 4")
        print("========================================")
        print("                                        ")

        try:
            choice=int(input("Enter your choice: "))
            if choice==1:
                add_student()
            elif choice==2:
                update_student()
            elif choice==3:
                remove_student()
            elif choice==4:
                admin_menu()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Error! Please enter a valid number!")

#Add Student function
def add_student():
    student_id=input("Enter new Student ID: ").strip()
    student_pass=input("Enter new Student Password: ").strip()

    try:
        with open ('Student.txt','r') as file:
            for line in file:
                data=line.strip().split(",")
                if data[0]==student_id:
                    print(f"Error! Student ID {student_id} already exists.")
                    return
    except FileNotFoundError:
        pass
    try:
        with open ('Student.txt','a') as file:
            file.write(f"{student_id},{student_pass}\n")
        print("Student added successfully!")
    except Exception as e:
        print(f"File Error! Cant write to file. {e}")

#Update Student function
def update_student():
    student_id=input("Enter Student ID to update: ").strip()

    updated=False
    records=[]
    
    try:
        with open('Student.txt','r') as file:
            for line in file:
                data=line.strip().split(',')
                if data[0]==student_id:
                    new_password=input(f"Enter new password: ").strip()
                    if new_password:
                        records.append(f"{student_id},{new_password}\n")
                        #\n used for next line
                        updated=True
                    else:
                        records.append(line)
                else:
                    records.append(line)
        
        if updated:
            with open('Student.txt','w') as file:
                file.writelines(records)
            print("Student updated successfully!")
        else:
            print("Student ID not found/No changes made.")
    except FileNotFoundError:
        print("Error! Student file not found.")

#Remove Student function
def remove_student():
    student_id=input("Enter Student ID to remove: ").strip()

    removed=False
    records=[]

    try:
        with open('Student.txt','r') as file:
            for line in file:
                data=line.strip().split(',')
                if data[0]!=student_id:
                    records.append(line)
                else:
                    removed=True

        if removed:
            with open('Student.txt','w') as file:
                file.writelines(records)
            print("Student removed successfully!")
        else:
            print("Student ID not found.")

    except FileNotFoundError:
        print("Error! Student file not found.")

#Couse Info Menu function 
def course_info():
    while True:
        print("                                       ")
        print("=======================================")
        print("Add Course, type 1")
        print("Update Course etails, type 2")
        print("Back to Admin Menu, type 3")
        print("=======================================")
        print("                                       ")

        try:
            choice=int(input("Enter you choice: "))
            if choice==1:
                add_course()
            elif choice==2:
                update_course()
            elif choice==3:
                admin_menu()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Error! Please enter a valid number!")

#Add Course function
def add_course():
    course_code=input("Enter Course Code: ").strip()
    course_name=input("Enter Course Name: ").strip()
    credit_hours=input("Enter Credit Hours: ").strip()

    if not course_code.isalnum() or not credit_hours.isdigit():
        print("Error! Course code must be alphanumeric and Credit hours must be numeric.")
        return
    try:
        with open('Courses.txt','r') as file:
            for line in file:
                if line.startswith(course_code+','):
                    print("Error! Course Code already exists.")
                    return
    except FileNotFoundError:
        pass
    try:
        with open('Courses.txt', 'a') as file:
            file.write(f"{course_code},{course_name},{credit_hours}\n")
        print("Course added successfully.")
    except Exception as e:
        print(f"File Error: {e}")

#Update Course function
def update_course():
    course_code=input("Enter Course Code to update: ").strip()
    
    updated=False
    records=[]
    try:
        with open('Courses.txt','r') as file:
            for line in file:
                data=line.strip().split(',')
                if data[0]==course_code:
                    print(f"Current Course Name: {data[1]}, Current Credits: {data[2]}")
                    new_course_name=input("Enter new course name: ").strip() or data[1]
                    new_credits=input("Enter new credit hours: ").strip() or data[2]

                    if new_credits.isdigit():
                        records.append(f"{course_code},{new_course_name},{new_credits}\n")
                        updated=True
                    else:
                        print("Validation Error! Credits Hours must be numeric.")
                        records.append(line)
                else:
                    records.append(line)
        if updated:
            with open('Courses.txt','w') as file:
                file.writelines(records)
            print("Course updated successfully!")
        elif not updated and len(records)>0:
            print("Course not found/No changes made")
    except FileNotFoundError:
        print("Error! Course file not found")

#View enrollment function
def view_enrollment():
    print("------All enrollment records------")
    try:
        with open('Enrollments.txt',"r") as file:
            lines=file.readlines()
            if not lines:
                print("No enrollments found.")
                return
            
            print(f"{'Student ID':<15} | {'Course Code':<15}")
            for line in lines:
                data=line.strip().split(',')
                if len(data)>=2:
                    print(f"{data[0]:<15}|{data[1]:<15}")
    except FileNotFoundError:
        print("Error! Enrollment file not found")

#Generate Menu function
def generate():
    while True:
        print("                                       ")
        print("=======================================")
        print("Generate Student Report, type 1")
        print("Generate Enrollment Summary, type 2")
        print("Back to Admin Menu, type 3")
        print("=======================================")
        print("                                       ")
    
        try:
            choice=int(input("Enter your choice: "))
            if choice==1:
                student_report()
            elif choice==2:
                enrollment_sum()
            elif choice==3:
                admin_menu()
            else:
                print("Invalid choice. Please try again")
        except ValueError:
            print("Error! Please enter a valid number!")

#Generate Student Report function
def student_report():
    try:
        with open('Student.txt','r') as file:
            lines=file.readlines()
        if not lines:
            print("No students registered.")
            return
        print(f"{'Student ID':<15} | {'Student Password':<25}")
        for line in lines:
            data = line.strip().split(',')
            if len(data) >= 2:
                print(f"{data[0]:<15} | {data[1]:<25}")
    except FileNotFoundError:
        print("Error! Student file not found.")

#Generate Enrollment Summary function
def enrollment_sum():
    course_counts={}

    try:
        with open('Enrollments.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) >= 2:
                    course_code = data[1]
                    if course_code in course_counts:
                        course_counts[course_code] += 1
                    else:
                        course_counts[course_code] = 1
                        
        if not course_counts:
            print("No enrollments to summarize.")
            return
            
        print(f"{'Course Code':<15} | {'Total Students Enrolled':<25}")
        print("-" * 45)
        for course, count in course_counts.items():
            print(f"{course:<15} | {count:<25}")
            
    except FileNotFoundError:
        print("Error: Enrollment records file not found.")


#Data Storage (text file)
STUDENT_FILE="Student.txt"
COURSES_FILE="Courses.txt"
ENROLLMENTS="Enrollments.txt"
RESULTS="Results.txt"

Maximum_Courses=3

#GPA
GPA={"A+":4.00,"A":3.70,"B+":3.30,"B":3.00,"C+":2.70,"C":2.30,"D+":1.70,"D":1.30,"F":1.00,"F-":0.00}



#Student Menu
def student_menu(student_id):
    while True:
        print("Welcome Student")
        print("=====================================")
        print("                                    ")
        print("Register Course, type 1")
        print("View Register Course type 2")
        print("View Result and GPA, type 3")
        print("Back to Student Menu, type 4")
        print("                                    ")
        print("=====================================")

        try:

            choice=int(input("Enter your choice:"))
        except ValueError:
            print("Invalid Choice Please try again")
            continue

        if choice==1:
            register_course(student_id)
        elif choice==2:
            view_registered_course(student_id)
        elif choice==3:
            view_result(student_id)
        elif choice==4:
            print("Back to Menu")
            student_menu
        else:
            print("Invalid Choice Please try again")

#Student Login
def student_login():
    print("\n---Student Login---")
    student_id=input("Enter Student ID:").strip()
    password=input("Enter Password:").strip()

    try:
        with open("Student.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==2:
                    sid,pwd=parts
                    if sid.strip().lower()==student_id.lower() and pwd.strip()==password:
                        print(f"Welcome {student_id}")
                        return student_id
    except FileNotFoundError:
        print("Error:Student.txt not fount")
        return None
    print("Invalid Student id or Password.")
    return None


#Register Courses
def register_course(student_id):
    print("\n-----Register Courses-----")

    courses={}
    try:
        with open("Courses.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==2:
                    courses[parts[0].strip()]=parts[1].strip()
    except FileNotFoundError:
        print("Error:Courses.txt not fount")
        return
        
    #students currents enrollments
    my_courses=[]
    try:
        with open("Enrollments.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==2 and parts[0].strip()+student_id.lower():
                    my_courses.append(parts[1].strip())
    except FileNotFoundError:
        pass

#check if the student registered for more than 3 course
    if len(my_courses)>=Maximum_Courses:
        print(f"You have already registered {Maximum_Courses} courses")
        return


#Show available course
    print(f"\n{'code'}{'Courses Name'}")
    for code,name in my_courses.items():
        tag="<enrollment>"if code in my_courses else""
        print(f"{'Code'}{name}{tag}")

    choice=int(input("Enter Courses.txt Code to Register(Press 0 to cancel):"))

    if choice=="0":
        print("Cancelling...")

    elif choice not in my_courses:
        print("Invalid Choice Please try again")
    elif choice in my_courses:
        print("You are already registered in this course")
    else:
        with open("Enrollments.txt","a") as f:
            f.write(f"{'student_id'},{choice}\n")
        print("Successfully registered: {courses[choice]}")

#View Register Courses
def view_registered_course(student_id):
    print("\n-----View Registered Courses-----")
    courses={}
    try:
        with open("Courses.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==2:
                    courses[parts[0].strip()]=parts[1].strip()
    except FileNotFoundError:
        print("Error:Courses.txt not fount")
        return

    my_courses=[]
    try:
        with open("Enrollments.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==2 and parts[0].strip()==student_id.lower():
                    my_courses.append(parts[1].strip())
    except FileNotFoundError:
        pass

    if not my_courses:
        print("You have not registered any courses")
        return

    print(f"\n{'code'}{'Courses Name'}")
    for i, code in enumerate(my_courses,1):
        if code in courses:
            print(f"{code},{courses[code]}")
        else:
            print(f"[Not Found]")
    print(f"Total Courses: {len(my_courses)}/{Maximum_Courses}")

#View GPA
def view_result(student_id):
    print("\n-----View My Results and GPA-----")
    courses={}
    try:
        with open("Courses.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==2:
                    courses[parts[0].strip()]=parts[1].strip()
    except FileNotFoundError:
        print("Error:Courses.txt not fount")
        return

    my_courses=[]
    try:
        with open("Enrollments.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==2 and parts[0].strip().lower()==student_id:
                    my_courses.append(parts[1].strip())
    except FileNotFoundError:
        pass

    if not my_courses:
        print("You have not registered any courses")
        return

    my_grades={}
    try:
        with open("Results.txt","r") as f:
            for line in f:
                parts=line.strip().split(",")
                if len(parts)==3 and parts[0].strip()==student_id:
                    my_grades[parts[1].strip()]=parts[2].strip()
    except FileNotFoundError:
        pass

    print(f"\n{'code'}{'Courses.txt Name'}{'Grade'}{'Points'}")
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

#Direct start the main menu function
if __name__ == "__main__":
    main_menu()
