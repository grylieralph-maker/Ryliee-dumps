"""add_student() - add a student with a grade.
update_grade() - update an existing student's grade.
get_average() - calculate the average grade.
display_students() - display all students and their grades.
Rules:
No global variables
Validate grades (1-100).
Don't allow duplicate student names.
Use functions to organize your program."""

students = {
    "Stan": {"grade": 90},
    "Butters": {"grade": 85},
    "Eric": {"grade": 78},
    "Kenny": {"grade": 80}
}

def add_student(students):
    while True:
        name = input("Enter Student Name: ").capitalize()
        if name in students or not name.isalpha():
            print("Invalid input. Please try again")
        else: 
            while True:
                try:
                    grade = float(input("Enter Student Grade: "))
                    students[name] = {'grade': grade}
                    print(f"{name} has been added to the list")
                    return students
                except ValueError:
                    print("Invalid input. Please try again")
       
        

def update_grade(students):
    print("Update Grade")
    while True:
        name = input("Enter Student Name: ").capitalize()
        if name in students:
            while True:
                change = float(input("Change Grade: "))
                if change >= 0 and change <= 100 :
                    students[name]['grade'] = change
                    print("Grade updated ")
                    return students[name]['grade']
                else: 
                    print("Invalid Input! Please Enter From(1-100)")
        else: 
            print("Student not found!")
            
        

def get_average(students):
    total = 0
    for value in students.values():
        total += value['grade']
    print(total / len(students))
        
        

def display_student(students):   
    for key, value in students.items(): 
        print(f"{key}: {value['grade']:g}")

while True:
    print("(1)Add\n(2)Update\n(3)Average\n(4)Display\n(5)Exit")
    try:
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_grade(students)
        elif choice == "3":
            get_average(students)
        elif choice == "4":
            display_student(students)
        elif choice == "5":
            print("Program finished.")
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid choice!")

            