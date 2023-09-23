class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Use the sorted function with a custom key to sort by CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of student objects
if __name__ == "__main__":
    # Sample student objects
    students = [
        Student("Ragoth", "A101", 3.8),
        Student("vinoth", "B102", 3.9),
        Student("malliga", "C103", 3.7),
        Student("ramasamy", "D104", 3.95),
    ]

    # Sort the students by CGPA in descending order
    sorted_students = sort_students(students)

    # Print the sorted list of students
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
