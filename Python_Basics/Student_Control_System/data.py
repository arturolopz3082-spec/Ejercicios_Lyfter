import csv
import os


FILE_NAME = "students.csv"

FIELD_NAMES = [
    "full_name",
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

    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
            writer.writeheader()
            writer.writerows(students)

        print(f"Los alumnos fueron guardados en el archivo: {FILE_NAME}.")
    except OSError:
        print("Hubo problemas para guardar el archivo")


def import_students_from_csv():
    print("Esto va a eliminar a los alumnos que no se guardaron previamente")
    if not os.path.exists(FILE_NAME):
        print("No hay archivo previo que se pueda importar")
        return []

    students = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = {
                    "full_name": row["full_name"],
                    "section": row["section"],
                    "spanish": float(row["spanish"]),
                    "english": float(row["english"]),
                    "social_studies": float(row["social_studies"]),
                    "science": float(row["science"]),
                }

                students.append(student)

        print("Se extrajo de manera correcta los alumnos del archivo.")
        return students

    except OSError:
        print("Hubo un error al importar el archivo")
        return []
    except KeyError:
        print("El archivo CSV no tiene el formato correcto.")
        return []
    except ValueError:
        print("El archivo CSV no tiene calificaciones válidas")
        return []