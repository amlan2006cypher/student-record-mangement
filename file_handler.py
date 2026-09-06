import csv
import json

from student import Student


def _student_from_values(values):
    """Create a Student object from seven common record values."""
    return Student(
        values[0],
        values[1],
        values[2],
        values[3],
        values[4],
        values[5],
        values[6],
    )


def read_txt(file_path):
    """Read student records from a comma-separated text file."""
    students = []
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line == "":
            continue
        values = line.split(",")
        cleaned_values = []
        for value in values:
            cleaned_values.append(value.strip())
        if len(cleaned_values) == 7:
            students.append(_student_from_values(cleaned_values))
    return students


def write_txt(students, file_path):
    """Write student records to a text file."""
    with open(file_path, "w", encoding="utf-8") as file:
        for student in students:
            values = student.to_list()
            line = (
                f"{values[0]}, {values[1]}, {values[2]}, {values[3]}, "
                f"{values[4]:g}, {values[5]:g}, {values[6]:g}\n"
            )
            file.write(line)


def read_csv(file_path):
    """Read student records from a CSV file and skip the header row."""
    students = []
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        first_row = True
        for row in reader:
            if first_row:
                first_row = False
                continue
            if len(row) == 7:
                students.append(_student_from_values(row))
    return students


def write_csv(students, file_path):
    """Write student records to a CSV file with a header."""
    header = [
        "Student_ID", "Name", "Department", "Semester",
        "Subject1", "Subject2", "Subject3"
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for student in students:
            values = student.to_list()
            writer.writerow(values)


def read_json(file_path):
    """Read student records from a JSON file."""
    students = []
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for record in data:
        marks = record["marks"]
        students.append(
            Student(
                record["student_id"],
                record["name"],
                record["department"],
                record["semester"],
                marks["subject1"],
                marks["subject2"],
                marks["subject3"],
            )
        )
    return students


def write_json(students, file_path):
    """Write student records to a JSON file."""
    data = []
    for student in students:
        data.append(student.to_dict())

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_students(file_path, file_format):
    """Load students according to the selected file format."""
    if file_format == "txt":
        return read_txt(file_path)
    if file_format == "csv":
        return read_csv(file_path)
    if file_format == "json":
        return read_json(file_path)
    raise ValueError("Unsupported format. Use txt, csv, or json.")


def save_students(students, file_path, file_format):
    """Save students according to the selected file format."""
    if file_format == "txt":
        write_txt(students, file_path)
    elif file_format == "csv":
        write_csv(students, file_path)
    elif file_format == "json":
        write_json(students, file_path)
    else:
        raise ValueError("Unsupported format. Use txt, csv, or json.")
