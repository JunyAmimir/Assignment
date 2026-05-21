def main_menu():
  while True:
#while True function used to infinite loop the main menu
    print("=========================================")
    print("                                                              ")
    print("Administrator Login, type 1")
    print("Student Login, type 2")
    print("Exit, type 3")
    print("                                                              ")
    print("=========================================")

    choice = int(input("Enter your choice="))
    if choice==1:
        Admin_id=input("Enter your Admin ID:")
        Admin_password=input("Enter your Admin Password:")
        file=open("Admin.txt","r")
        correct=file.read().strip()
        file.close()
        if Admin_id==correct[0] and Admin_password==correct[1]:
            print("Login successful!")
        else:
            print("Invalid Admin ID or Password. Please try again.")
    elif choice==2:
        Student_id=input("Enter your Student ID:")
        Student_password=input("Enter your Student Password:")
        file=open("Student.txt","r")
        correct=file.read().strip()
        file.close()
        if Student_id==correct[0] and Student_password==correct[1]:
            print("Login successful!")
        else:
            print("Invalid Student ID or Password. Please try again.")
    elif choice==3:
        print("Thank you for using the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

#Direct start the main menu function
main_menu()