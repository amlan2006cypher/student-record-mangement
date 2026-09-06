import argparse

from manager import StudentManager
from student import Student


def build_parser():
    parser = argparse.ArgumentParser(
        description="Student Record Management and Search System"
    )
    parser.add_argument(
        "--file",
        required=True,
        help="Input student data file."
    )
    parser.add_argument(
        "--format",
        required=True,
        choices=["txt", "csv", "json"],
        help="Input file format."
    )
    parser.add_argument(
        "--action",
        required=True,
        choices=[
            "display", "search-id", "search-name", "search-department",
            "search-average", "add", "remove", "update-marks", "save"
        ],
        help="Operation to perform."
    )
    parser.add_argument("--id", type=int, help="Student ID.")
    parser.add_argument("--name", help="Student name.")
    parser.add_argument("--department", help="Student department.")
    parser.add_argument("--average", type=float, help="Minimum average for condition search.")
    parser.add_argument("--subject1", type=float, help="Subject 1 marks.")
    parser.add_argument("--subject2", type=float, help="Subject 2 marks.")
    parser.add_argument("--subject3", type=float, help="Subject 3 marks.")
    parser.add_argument("--semester", type=int, help="Student semester.")
    parser.add_argument(
        "--output",
        help="Output file used with the save action."
    )
    parser.add_argument(
        "--output-format",
        choices=["txt", "csv", "json"],
        help="Output format used with the save action."
    )
    return parser


def print_results(results):
    if not results:
        print("No matching student records found.")
        return

    if isinstance(results, list):
        for student in results:
            print(student.display_student())
    else:
        print(results.display_student())


def create_student_from_args(args):
    required_values = [
        args.id, args.name, args.department, args.semester,
        args.subject1, args.subject2, args.subject3
    ]
    if any(value is None for value in required_values):
        raise ValueError(
            "The add action requires --id, --name, --department, "
            "--semester, --subject1, --subject2, and --subject3."
        )

    return Student(
        args.id,
        args.name,
        args.department,
        args.semester,
        args.subject1,
        args.subject2,
        args.subject3,
    )


def main():
    parser = build_parser()
    args = parser.parse_args()

    manager = StudentManager()
    manager.load_from_file(args.file, args.format)

    if args.action == "display":
        print("All Student Records")
        print("-" * 80)
        for line in manager.display_all_students():
            print(line)

    elif args.action == "search-id":
        if args.id is None:
            raise ValueError("--id is required for search-id.")
        print_results(manager.search_student(args.id))

    elif args.action == "search-name":
        if args.name is None:
            raise ValueError("--name is required for search-name.")
        print_results(manager.search_by_name(args.name))

    elif args.action == "search-department":
        if args.department is None:
            raise ValueError("--department is required for search-department.")
        print_results(manager.search_by_department(args.department))

    elif args.action == "search-average":
        if args.average is None:
            raise ValueError("--average is required for search-average.")
        print(f"Students with average greater than {args.average:.2f}")
        print("-" * 80)
        print_results(manager.search_by_average(args.average))

    elif args.action == "add":
        student = create_student_from_args(args)
        if manager.add_student(student):
            print("Student added successfully.")
            print(student.display_student())
            if args.output and args.output_format:
                manager.save_to_file(args.output, args.output_format)
                print(f"Updated records saved to {args.output}.")
        else:
            print("A student with this Student ID already exists.")

    elif args.action == "remove":
        if args.id is None:
            raise ValueError("--id is required for remove.")
        if manager.remove_student(args.id):
            print(f"Student {args.id} removed successfully.")
            if args.output and args.output_format:
                manager.save_to_file(args.output, args.output_format)
                print(f"Updated records saved to {args.output}.")
        else:
            print(f"Student {args.id} was not found.")

    elif args.action == "update-marks":
        if args.id is None or args.subject1 is None or args.subject2 is None or args.subject3 is None:
            raise ValueError(
                "update-marks requires --id, --subject1, --subject2, and --subject3."
            )
        student = manager.search_student(args.id)
        if student is None:
            print(f"Student {args.id} was not found.")
        else:
            student.update_marks(args.subject1, args.subject2, args.subject3)
            print("Marks updated successfully.")
            print(student.display_student())
            if args.output and args.output_format:
                manager.save_to_file(args.output, args.output_format)
                print(f"Updated records saved to {args.output}.")

    elif args.action == "save":
        output_file = args.output
        output_format = args.output_format
        if output_file is None or output_format is None:
            raise ValueError("save requires --output and --output-format.")
        manager.save_to_file(output_file, output_format)
        print(f"Saved {len(manager.students)} student records to {output_file}.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, FileNotFoundError, KeyError) as error:
        print(f"Error: {error}")
