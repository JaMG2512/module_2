

while True:
    last_name = input("Enter the student's last name (ZZZ to quit): ")

    if last_name == "ZZZ":
        print("Program terminated.")
        break

    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    print(f"\nStudent: {first_name} {last_name}")

    if gpa >= 3.5:
        print("Congratulations! The student has made the Dean's List.")

    if gpa >= 3.25:
        print("Congratulations! The student has made the Honor Roll.")

    print()
