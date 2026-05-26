def admin_main_menu():
    print("Welcome,Admin")
    print("=====================================")
    print("                                    ")
    print("Manage Students Record, type 1")
    print("Manage Course Information, type 2")
    print("View Enrolment Record, type 3")
    print("Generate Reports, type 4")
    print("Back to Main Menu, type 5")
    print("                                    ")
    print("=====================================")
    
    choice=int(input("Enter your choice: "))
    if choice==1:
        student_record()
    elif choice==2:
        course_info()
    elif choice==3:
        view_enrolment()
    elif choice==4:
        generate_report()
    elif choice==5:
        main_menu()
    else:
        print("Invalid choice. Please try again.")

def student_record():
    print("========================================")
    print("Add student information, type 1")
    print("Update student information, type 2")
    print("Remove student information, type 3")
    print("Back to admin main menu, type 4")
    print("========================================")

    choice=int(input("Enter your choice: "))

def course_info():
    print("=================================")
    print("Add course, type 1")
    print("Update course details, type 2")
    print("Back to admin main menu, type 3")
    print("=================================")

    choice=int(input("Enter you choice: "))
