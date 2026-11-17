import os

filename = "students.txt"

def display_students():
    if not os.path.exists(filename):
        print("No student records found.")
        return

    with open(filename, "r") as file:
        records = file.readlines()

    if not records:
        print("No student records found.")
    else:
        for record in records:
            print(record.strip())

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    if not roll.isdigit() or not marks.isdigit():
        print("Roll number and marks must be numeric.")
        return

    with open(filename, "a+") as file:
        file.seek(0)
        for record in file:
            if record.split(",")[0] == roll:
                print("Roll number already exists.")
                return

        file.write(roll + "," + name + "," + marks + "\n")

    print("Student added successfully.")

def search_student():
    roll = input("Enter roll number to search: ")

    if not os.path.exists(filename):
        print("No student records found.")
        return

    with open(filename, "r") as file:
        for record in file:
            data = record.strip().split(",")

            if data[0] == roll:
                print("Roll No:", data[0])
                print("Name:", data[1])
                print("Marks:", data[2])
                return

    print("Student not found.")

def update_student():
    roll = input("Enter roll number to update: ")

    if not os.path.exists(filename):
        print("No student records found.")
        return

    with open(filename, "r") as file:
        records = file.readlines()

    found = False

    for i in range(len(records)):
        data = records[i].strip().split(",")

        if data[0] == roll:
            name = input("Enter new name: ")
            marks = input("Enter new marks: ")

            if not name or not marks.isdigit():
                print("Invalid input.")
                return

            records[i] = roll + "," + name + "," + marks + "\n"
            found = True
            break

    if found:
        with open(filename, "w") as file:
            file.writelines(records)
        print("Student updated successfully.")
    else:
        print("Student not found.")

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
