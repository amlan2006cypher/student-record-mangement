class Student:
    """Represents one student and provides student-level operations."""

    PASS_MARK = 40

    def __init__(self, student_id, name, department, semester, subject1, subject2, subject3):
        self.student_id = int(student_id)
        self.name = name.strip()
        self.department = department.strip()
        self.semester = int(semester)
        self.marks = {
            "subject1": float(subject1),
            "subject2": float(subject2),
            "subject3": float(subject3),
        }

    def calculate_total(self):
        """Return the total marks in the three subjects."""
        return (
            self.marks["subject1"]
            + self.marks["subject2"]
            + self.marks["subject3"]
        )

    def calculate_average(self):
        """Return the average marks."""
        return self.calculate_total() / 3

    def get_result(self):
        """Return PASS only when the student passes all three subjects."""
        if (
            self.marks["subject1"] >= self.PASS_MARK
            and self.marks["subject2"] >= self.PASS_MARK
            and self.marks["subject3"] >= self.PASS_MARK
        ):
            return "PASS"
        return "FAIL"

    def update_marks(self, subject1, subject2, subject3):
        """Modify the marks of the student."""
        self.marks["subject1"] = float(subject1)
        self.marks["subject2"] = float(subject2)
        self.marks["subject3"] = float(subject3)

    def display_student(self):
        """Return a formatted representation of the student's details."""
        return (
            f"ID: {self.student_id} | Name: {self.name} | "
            f"Department: {self.department} | Semester: {self.semester} | "
            f"Marks: {self.marks['subject1']:.1f}, "
            f"{self.marks['subject2']:.1f}, {self.marks['subject3']:.1f} | "
            f"Total: {self.calculate_total():.1f} | "
            f"Average: {self.calculate_average():.2f} | "
            f"Result: {self.get_result()}"
        )

    def to_list(self):
        """Return the student as a list suitable for TXT/CSV writing."""
        return [
            self.student_id,
            self.name,
            self.department,
            self.semester,
            self.marks["subject1"],
            self.marks["subject2"],
            self.marks["subject3"],
        ]

    def to_dict(self):
        """Return the student as a dictionary suitable for JSON writing."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "department": self.department,
            "semester": self.semester,
            "marks": {
                "subject1": self.marks["subject1"],
                "subject2": self.marks["subject2"],
                "subject3": self.marks["subject3"],
            },
        }
