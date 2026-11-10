students = {
    "Stan": {"grade": 90},
    "Butters": {"grade": 85},
    "Eric": {"grade": 78},
    "Kenny": {"grade": 80}
}

def add_student(students):
    print(10*"=","ADD STUDENT","="*10)
    while True:
        name = input("Enter Student Name: ").title()
        if name in students or not name.replace(" ","").isalpha():
            print("Student already listed or Invalid input. Please try again")
        else: 
            while True:
                try:
                    grade = float(input("Enter Student Grade: "))
                    if grade >=0 and grade <=100:
                        students[name] = {'grade': grade}
                        print(f"{name} has been added to the list\n")
                        return students
                    else:
                        print("Invalid input. Please enter from(0-100)")
                except ValueError:
                    print("Invalid input. Please try again")
       
        

def update_grade(students):
    print(10*"=","UPDATE GRADES","="*10)
    while True:
        name = input("Enter Student Name: ").title()
        if name in students:
            while True:
                try:
                    change = float(input("Change Grade: "))
                    if change >= 0 and change <= 100 :
                        students[name]['grade'] = change
                        print("Grade updated successfully\n")
                        return students[name]['grade']
                    else: 
                        print("Invalid Input! Please enter from(0-100)")
                except ValueError:
                    print("Invalid input! Please enter from(0-100)")
        else: 
            print("Student not found! Try again")
            
        

def get_average(students):
    print(10*"=","AVERAGE","="*10)
    total = 0
    for value in students.values():
        total += value['grade']
    print(f"Overall average: {total / len(students)}\n")
        
        

def display_students(students):   
    print(10*"=","STUDENTS LIST","="*10)
    for key, value in students.items(): 
        print(f"{key}: {value['grade']:g}\n")

while True:
    print("(1)Add Student\n(2)Update Student's Grade\n(3)Calculate Average\n(4)Display List\n(5)Exit")
    try:
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_grade(students)
        elif choice == "3":
            get_average(students)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            print("\n===== PROGRAM FINISHED =====")
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid choice!")

            