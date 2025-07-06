class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        for student in self.students:
            if student.name == name:
                print(f"{name} already exists.")
                return
        self.students.append(Student(name))
        print(f"Added {name}")

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def record_grade(self, name, grade):
        student = self.find_student(name)
        if student:
            student.add_grade(grade)
            print(f"Added grade {grade} for {name}")
        else:
            print(f"{name} not found")

    def calculate_average_all(self):
        if not self.students:
            return 0
        total = 0
        count = 0
        for student in self.students:
            total += student.calculate_average()
            count += 1
        return total / count

    def save_data(self, filename):
        with open(filename, "w") as file:
            for student in self.students:
                avg = student.calculate_average()
                file.write(f"{student.name}: {avg:.2f}\n")
        print(f"Data saved to {filename}")

def main():
    manager = GradeManager()

    while True:
        print("\nMenu:")
        print("1. Add a new student")
        print("2. Record a grade for a student")
        print("3. Calculate the average grade of all students")
        print("4. Save the data to a file")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student name: ")
            manager.add_student(name)

        elif choice == '2':
            name = input("Enter student name: ")
            try:
                grade = float(input("Enter grade: "))
                manager.record_grade(name, grade)
            except ValueError:
                print("Invalid grade. Please enter a number.")

        elif choice == '3':
            avg_all = manager.calculate_average_all()
            print(f"Average grade of all students: {avg_all:.2f}")

        elif choice == '4':
            filename = input("Enter filename to save data: ")
            manager.save_data(filename)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
