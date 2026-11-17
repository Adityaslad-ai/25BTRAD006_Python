attendance = {}

while True:
    print("\n===== ATTENDANCE TRACKER =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Display Attendance")
    print("4. Check Attendance Percentage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")

        if name not in attendance:
            attendance[name] = []
            print("Student added successfully.")
        else:
            print("Student already exists.")

    # Mark attendance
    elif choice == "2":
        name = input("Enter student name: ")

        if name in attendance:
            status = input("Enter P for Present or A for Absent: ").upper()

            if status == "P" or status == "A":
                attendance[name].append(status)
                print("Attendance updated.")
            else:
                print("Invalid status.")
        else:
            print("Student not found.")

    # Display attendance
    elif choice == "3":
        print("\n===== ATTENDANCE RECORD =====")

        if len(attendance) == 0:
            print("No students added.")
        else:
            for name, records in attendance.items():
                print(name, ":", records)

    # Calculate percentage
    elif choice == "4":
        threshold = float(input("Enter attendance threshold (%): "))

        print("\n===== ATTENDANCE PERCENTAGE =====")

        for name, records in attendance.items():
            total_classes = len(records)
            present_classes = records.count("P")

            if total_classes > 0:
                percentage = (present_classes / total_classes) * 100
            else:
                percentage = 0

            print(name, ":", round(percentage, 2), "%")

            if percentage < threshold:
                print("  -> Below attendance threshold")

    # Exit
    elif choice == "5":
        print("Thank you for using Attendance Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
