#Admin Main Menu function
def admin_main_menu():
    while True:
        print("Welcome,Admin")
        print("====================================")
        print("                                    ")
        print("Manage Students Record, type 1")
        print("Manage Course Information, type 2")
        print("View Enrolment Record, type 3")
        print("Generate Reports, type 4")
        print("Back to Main Menu, type 5")
        print("                                    ")
        print("====================================")
    
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

#Storage
Students_Data='Students.txt'
Course_Data='Course.txt'
Enrollment_Data='Enrollments.txt'

#Student Record Menu function
def student_record():
    while True:
        print("                                        ")
        print("========================================")
        print("Add Student Information, type 1")
        print("Update Student Information, type 2")
        print("Remove Student Information, type 3")
        print("Back to Admin Main Menu, type 4")
        print("========================================")
        print("                                        ")

        choice=int(input("Enter your choice: "))
        if choice==1:
            add_student()
        elif choice==2:
            update_student()
        elif choice==3:
            remove_student()
        elif choice==4:
            admin_main_menu()
        else:
            print("Invalid choice. Please try again.")

#Add Student function
def add_student():
    student_id=input("Enter new Student ID: ").strip()
    student_pass=input("Enter new Student Password: ").strip()

    try:
        with open ('Students.txt','r') as file:
            for line in file:
                data=line.strip().split(",")
                if data[0]==student_id:
                    print(f"Error! Student ID {student_id} already exists.")
                    return
    except FileNotFoundError:
        pass
    try:
        with open ('Students.txt','a') as file:
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
        with open('Students.txt','r') as file:
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
            with open('Students.txt','w') as file:
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
        with open('Students.txt','r') as file:
            for line in file:
                data=line.strip().split(',')
                if data[0]!=student_id:
                    records.append(line)
                else:
                    removed=True

        if removed:
            with open('Students.txt','w') as file:
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
        print("Back to Admin Main Menu, type 3")
        print("=======================================")
        print("                                       ")

        choice=int(input("Enter you choice: "))
        if choice==1:
            add_course()
        elif choice==2:
            update_course()
        elif choice==3:
            admin_main_menu()
        else:
            print("Invalid choice. Please try again.")

#Add Course function
def add_course():
    course_code=input("Enter Course Code: ").strip()
    course_name=input("Enter Course Name: ").strip()
    credit_hours=input("Enter Credit Hours: ").strip()

    if not course_code.isalnum() or not credit_hours.isdigit():
        print("Error! Course code must be alphanumeric and Credit hours must be numeric.")
        return
    try:
        with open('Course.txt','r') as file:
            for line in file:
                if line.startswith(course_code+','):
                    print("Error! Course Code already exists.")
                    return
    except FileNotFoundError:
        pass
    try:
        with open('Course.txt', 'a') as file:
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
        with open('Course.txt','r') as file:
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
            with open('Course.txt','w') as file:
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
        print("Back to Admin Main Menu, type 3")
        print("=======================================")
        print("                                       ")
    
        choice=int(input("Enter your choice: "))
        if choice==1:
            student_report()
        elif choice==2:
            enrollment_sum()
        elif choice==3:
            admin_main_menu()
        else:
            print("Invalid choice. Please try again")

#Generate Student Report function
def student_report():
    try:
        with open('Students.txt','r') as file:
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

admin_main_menu()