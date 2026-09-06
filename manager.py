class StudentManager:
    """Manages a collection of Student objects."""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        """Add a student if the Student ID is not already present."""
        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                return False
        self.students.append(student)
        return True

    def remove_student(self, student_id):
        """Remove a student using Student ID."""
        for index in range(len(self.students)):
            if self.students[index].student_id == int(student_id):
                del self.students[index]
                return True
        return False

    def search_student(self, student_id):
        """Search for one student by Student ID using a basic loop."""
        for student in self.students:
            if student.student_id == int(student_id):
                return student
        return None

    def search_by_name(self, name):
        """Search students by name using loops and string comparison."""
        results = []
        target = name.strip().lower()
        for student in self.students:
            if student.name.lower() == target:
                results.append(student)
        return results

    def search_by_department(self, department):
        """Search students by department using loops and conditions."""
        results = []
        target = department.strip().lower()
        for student in self.students:
            if student.department.lower() == target:
                results.append(student)
        return results

    def search_by_average(self, minimum_average):
        """Return students whose average is greater than the given value."""
        results = []
        for student in self.students:
            if student.calculate_average() > float(minimum_average):
                results.append(student)
        return results

    def display_all_students(self):
        """Return all students in a formatted list."""
        output = []
        for student in self.students:
            output.append(student.display_student())
        return output

    def load_from_file(self, file_path, file_format):
        """Load students from a TXT, CSV, or JSON file."""
        from file_handler import load_students
        loaded_students = load_students(file_path, file_format)
        self.students = []
        for student in loaded_students:
            self.add_student(student)
        return len(self.students)

    def save_to_file(self, file_path, file_format):
        """Save all students to a TXT, CSV, or JSON file."""
        from file_handler import save_students
        save_students(self.students, file_path, file_format)
