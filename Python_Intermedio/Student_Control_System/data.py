import csv
import os
from actions import Student

FILE_NAME = "students.csv"

FIELD_NAMES = [
    "name",
    "section",
    "spanish",
    "english",
    "social_studies",
    "science",
]


def export_students_to_csv(students):
    if not students:
        print("No hay estudiantes a exportar.")
        return

    file_exists = os.path.exists(FILE_NAME)
    file_is_empty = (
            not file_exists or os.path.getsize(FILE_NAME) == 0
    )

    try:
        with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
            if file_is_empty:
                writer.writeheader()
            for student in students:
                row = {
                    'name': student.name,
                    'section': student.section,
                    'spanish': student.spanish,
                    'english': student.english,
                    'social_studies': student.social_studies,
                    'science': student.science,
                }
                writer.writerow(row)

        print(f"Los alumnos fueron guardados en el archivo: {FILE_NAME}.")
    except OSError as error:
        print(f"Hubo problemas para guardar el archivo con el error: {error}")


def import_students_from_csv():
    if not os.path.exists(FILE_NAME):
        print("No hay archivo previo para importar.")
        return []

    students = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    row["name"],
                    row["section"],
                    row["spanish"],
                    row["english"],
                    row["social_studies"],
                    row["science"],
                )

                students.append(student)

        print("Los estudiantes fueron importados de manera correcta.")
        return students

    except OSError:
        print("Ocurrió un error al importar los alumnos.")
        return []
    except KeyError:
        print("El archivo CSV no tiene el nombre correcto")
        return []
    except ValueError:
        print("El archivo CSV tiene calificaciones no válidas.")
        return []