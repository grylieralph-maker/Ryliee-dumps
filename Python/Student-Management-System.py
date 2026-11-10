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
    add = input("Enter Student Name: ")
    if name not in students:
        grade = float(input("Enter Student Grade: "))
        students[name] = {'grade': grade}
        return students
    else: 
        print("Student Already Listed")
    return(students)    
        

def update_grade():
    print("Update Grade")
    name = input("Enter Student Name: ")
    if name in students:
        change = float(input("Change Grade: "))
        if change >= 0 and change <= 100 :
            students[name]['grade'] = change
            return students[name]['grade']
        else: 
            print("Invalid Input! Please Enter From(1-100)")
    else: 
        print("Student not found!")
        
        

def get_average():
    total = 0
    for value in students.values():
        total += value['grades']
    return total / len(students)
        
        

def display_student():   
    for key, value in students.items(): 
        print(f"{key}: {value['grade']}")

display_student()        