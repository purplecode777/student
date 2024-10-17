# Initialize an empty dictionary to store student information
student_dict = {}

def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    marks = float(input("Enter student's marks (out of 100): "))

    # Validate marks
    while marks < 0 or marks > 100:
        print("Invalid marks. Please enter between 0 and 100.")
        marks = float(input("Enter student's marks (out of 100): "))

    student_dict[name] = {"Age": age, "Marks": marks}
    print(f"Student {name} added successfully.")

def update_student():
    name = input("Enter student's name: ")

    if name in student_dict:
        print("1. Update Age")
        print("2. Update Marks")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            age = int(input("Enter new age: "))
            student_dict[name]["Age"] = age
        elif choice == 2:
            marks = float(input("Enter new marks (out of 100): "))

            # Validate marks
            while marks < 0 or marks > 100:
                print("Invalid marks. Please enter between 0 and 100.")
                marks = float(input("Enter new marks (out of 100): "))

            student_dict[name]["Marks"] = marks
        print(f"Student {name} updated successfully.")
    else:
        print(f"Student {name} not found.")

def display_students():
    if student_dict:
        print("Student Details:")
        for name, details in student_dict.items():
            age = details["Age"]
            marks = details["Marks"]
            grade = evaluate_grade(marks)
            print(f"Name: {name}, Age: {age}, Marks: {marks}, Grade: {grade}")
    else:
        print("No students added.")

def evaluate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Display Students")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            update_student()
        elif choice == 3:
            display_students()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
