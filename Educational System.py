students = {}

def menu():
    print("\n--- Educational System ---")
    print("1. Add student details.")
    print("2. Display student details.")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice not in ["1","2","3"]:
        print("Invalid choice. Please select a valid option.")
        continue

    if choice == "1":
        roll_no = input("Enter roll number: ")

        if roll_no in students:
            print("Student already exists")
        else:
            name = input("Enter your name: ")
            marks = int(input("Enter your marks: "))
            students[roll_no] = {"Name": name, "Marks": marks}
            print("Student details added successfully.")

    elif choice == "2":
        if not students:
            print("No student records available.")
        else:
            print("\n--- Student Details ---")
            for roll_no,details in students.items():
                print(f"Roll No: {roll_no}")
                print(f"Name : {details["Name"]}")
                print(f"Marks : {details["Marks"]}")
                print("-"*20)

    elif choice == "3":
        print("Thank you for using the Educational System. Goodbye!")
        break