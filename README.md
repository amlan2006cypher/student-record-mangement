# Student Record Management & Search System

## A. Title

**Student Record Management & Search System**

## B. Objective

This project implements a Student Record Management and Search System in Python. It demonstrates Object-Oriented Programming, file handling with TXT/CSV/JSON files, and basic searching/filtering using loops, conditions, and comparisons.

The implementation follows the assignment requirements by separating the `Student` object from the `StudentManager` that manages multiple students. The project also uses command-line arguments instead of hard-coded input file names.

## C. Features

- Create and manage `Student` objects.
- Calculate total marks.
- Calculate average marks.
- Determine pass/fail status.
- Update a student's marks.
- Add and remove students.
- Display all student records.
- Search by Student ID.
- Search by Name.
- Search by Department.
- Condition-based search for average marks greater than a supplied value.
- Read and write TXT files.
- Read and write CSV files using Python's `csv` module.
- Read and write JSON files using Python's `json` module.
- Command-line interface using `argparse`.
- Sample data containing 5 student records.
- Sample output files/screenshots for demonstration.

## D. Project Structure

```text
student-record-system/
├── main.py
├── student.py
├── manager.py
├── file_handler.py
├── data/
│   ├── students.txt
│   ├── students.csv
│   └── students.json
├── screenshots/
│   ├── display_output.png
│   └── search_output.png
├── README.md
└── .gitignore
```

### Python files

- `main.py` → Command-line interface and program execution.
- `student.py` → `Student` class, attributes, calculations, result checking, updating marks, and conversion methods.
- `manager.py` → `StudentManager` class for managing multiple `Student` objects and performing searches.
- `file_handler.py` → TXT, CSV, and JSON reading/writing functions.

## E. Requirements

- Python 3.8 or later.
- No external Python packages are required.
- Only Python standard-library modules are used: `argparse`, `csv`, and `json`.
- Pandas and NumPy are not used.

## F. How to Run

Open a terminal in the project directory.

### 1. Display records from TXT

```bash
python main.py --file data/students.txt --format txt --action display
```

### 2. Display records from CSV

```bash
python main.py --file data/students.csv --format csv --action display
```

### 3. Display records from JSON

```bash
python main.py --file data/students.json --format json --action display
```

### 4. Search by Student ID

```bash
python main.py --file data/students.csv --format csv --action search-id --id 103
```

### 5. Search by Name

```bash
python main.py --file data/students.csv --format csv --action search-name --name Amit
```

### 6. Search by Department

```bash
python main.py --file data/students.csv --format csv --action search-department --department "Computer Science"
```

### 7. Condition-based average search

The assignment asks for a condition such as students having an average greater than a given value.

```bash
python main.py --file data/students.csv --format csv --action search-average --average 80
```

### 8. Add a student

```bash
python main.py --file data/students.csv --format csv --action add --id 106 --name "Neha" --department "Physics" --semester 1 --subject1 88 --subject2 79 --subject3 91
```

The `add` action changes the in-memory `StudentManager`. To persist the addition in the same command, provide `--output` and `--output-format`.

Example:

```bash
python main.py --file data/students.csv --format csv --action add --id 106 --name "Neha" --department "Physics" --semester 1 --subject1 88 --subject2 79 --subject3 91 --output data/students_updated.csv --output-format csv
```

### 9. Remove a student

```bash
python main.py --file data/students.csv --format csv --action remove --id 105 --output data/students_updated.csv --output-format csv
```

### 10. Update marks from a loaded JSON file

```bash
python main.py --file data/students.json --format json --action update-marks --id 104 --subject1 95 --subject2 93 --subject3 96 --output data/students_updated.json --output-format json
```

### 11. Save records to another CSV file

```bash
python main.py --file data/students.csv --format csv --action save --output data/students_updated.csv --output-format csv
```

### 12. Save records to JSON

```bash
python main.py --file data/students.csv --format csv --action save --output data/students_updated.json --output-format json
```

### Important note about separate commands

Each command starts a fresh program execution and loads the selected input file. The `add`, `remove`, and `update-marks` actions can persist their changes immediately when `--output` and `--output-format` are supplied. The separate `save` action is also available when you only want to copy the loaded collection to another format/file.

## G. Input and Output

### Input

The program accepts:

- Student ID
- Name
- Department
- Semester
- Marks in three subjects
- A file path and file format through command-line arguments
- Search values such as ID, name, department, or minimum average

### Input files

Sample files are provided in `data/`:

- `students.txt`
- `students.csv`
- `students.json`

Each sample file contains the same 5 student records.

### Output

The program displays student records and search results in the terminal. The `save` action creates the requested output file.

### Sample output

```text
All Student Records
--------------------------------------------------------------------------------
ID: 101 | Name: Rahul | Department: Computer Science | Semester: 1 | Marks: 78.0, 82.0, 69.0 | Total: 229.0 | Average: 76.33 | Result: PASS
ID: 102 | Name: Priya | Department: Computer Science | Semester: 1 | Marks: 91.0, 87.0, 94.0 | Total: 272.0 | Average: 90.67 | Result: PASS
ID: 103 | Name: Amit | Department: Mathematics | Semester: 1 | Marks: 65.0, 71.0, 68.0 | Total: 204.0 | Average: 68.00 | Result: PASS
ID: 104 | Name: Sneha | Department: Physics | Semester: 2 | Marks: 88.0, 76.0, 92.0 | Total: 256.0 | Average: 85.33 | Result: PASS
ID: 105 | Name: Arjun | Department: Computer Science | Semester: 2 | Marks: 55.0, 63.0, 59.0 | Total: 177.0 | Average: 59.00 | Result: PASS
```

The pass criterion implemented in `Student.get_result()` is **40 marks or more in every subject**.

## H. OOP Concepts Used

### Classes

Two main classes are used:

- `Student` represents one student.
- `StudentManager` manages multiple student objects.

### Objects

Each input record is converted into a `Student` object. `StudentManager.students` stores multiple `Student` objects.

### Constructors

Both classes use `__init__()` constructors to initialize their data.

### Attributes

`Student` contains:

- `student_id`
- `name`
- `department`
- `semester`
- `marks`

`StudentManager` contains:

- `students`

### Instance methods

Examples include:

- `calculate_total()`
- `calculate_average()`
- `get_result()`
- `update_marks()`
- `display_student()`
- `add_student()`
- `remove_student()`
- `search_student()`
- `search_by_name()`
- `search_by_department()`
- `search_by_average()`
- `display_all_students()`
- `load_from_file()`
- `save_to_file()`

No complicated inheritance is used because it is not required by the assignment.

## I. File Handling Concepts Used

### TXT

`file_handler.py` uses:

- `open()`
- `with open(...)`
- `readlines()`
- `write()`
- `r` and `w` file modes

The TXT file contains comma-separated records.

### CSV

The built-in `csv` module is used:

- `csv.reader()` reads records.
- `csv.writer()` writes records.
- The first row is handled as the header.

### JSON

The built-in `json` module is used:

- `json.load()` reads JSON data.
- `json.dump()` writes updated JSON data.
- Dictionaries and lists represent the JSON structure.

No external data-processing libraries are used.

## J. Searching Concepts Used

The required searches are implemented in `StudentManager` using basic Python logic.

- **Student ID:** a `for` loop compares each student's ID with the requested ID.
- **Name:** a loop compares lowercase names for case-insensitive matching.
- **Department:** a loop compares lowercase department names.
- **Average condition:** a loop calculates each student's average and checks whether it is greater than the supplied value.

The implementation deliberately avoids search-specific built-in functions or external libraries.

## K. Learning Outcome / Conclusion

This project provides practical experience with Python classes, objects, constructors, instance methods, file handling, command-line arguments, and basic searching logic. A major part of the implementation is separating responsibilities: `Student` handles one student's data and operations, while `StudentManager` handles the collection of students. Working with three file formats also demonstrates how the same Python objects can be stored and reconstructed from different representations.

The main implementation challenge is keeping the file-specific code separate from the student-management logic while ensuring that TXT, CSV, and JSON records are converted into the same `Student` objects.


