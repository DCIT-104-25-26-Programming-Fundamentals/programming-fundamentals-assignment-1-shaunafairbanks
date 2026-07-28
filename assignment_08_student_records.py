
# List to store student records
students = []


# Function to add a student
def add_student():
    name = input("Student name: ")
    student_id = input("Student ID: ")

    num_scores = int(input("How many scores? "))
    scores = []

    for i in range(num_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)
    print(f'Student "{name}" added successfully.')


# Function to display all students
def display_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print("-" * 70)
    print(f"{'Name':20}{'ID':15}{'Scores':20}{'Average'}")
    print("-" * 70)

    for student in students:
        average = round(sum(student["scores"]) / len(student["scores"]), 2)
        scores = ", ".join(str(score) for score in student["scores"])

        print(f"{student['name']:20}{student['id']:15}{scores:20}{average:.2f}")

    print("-" * 70)


# Function to calculate the average score of one student
def calculate_average():
    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            average = round(sum(student["scores"]) / len(student["scores"]), 2)
            print(f"{student['name']}'s average score: {average:.2f}")
            return

    print("Error: Student ID not found.")


# Main function
def main():
    while True:
        print("\n================================")
        print("   STUDENT RECORD SYSTEM MENU")
        print("================================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")


# Run the program
main()