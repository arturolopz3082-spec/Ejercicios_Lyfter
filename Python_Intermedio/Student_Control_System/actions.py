import re

SUBJECTS = ["español", "inglés", "estudios_sociales", "ciencias"]

class Student:
    def __init__(self, name, español, inglés, estudios_sociales, ciencias, section):
        self.name = name
        self.español = español
        self.inglés = inglés
        self.estudios_sociales = estudios_sociales
        self.ciencias = ciencias
        self.section = section

def create_student(students_list):
    name = get_valid_name()
    español = get_valid_grade("español")
    inglés = get_valid_grade("inglés")
    estudios_sociales = get_valid_grade("estudios_sociales")
    ciencias = get_valid_grade("ciencias")
    section = get_valid_section()
    student = Student(name, español, inglés, estudios_sociales, ciencias, section)
    print(student.__dict__)



def is_valid_name(name):
    return bool(name.strip() and not any(char.isdigit() for char in name))

def get_valid_name():
    while True:
        full_name = input("Ingrese el nombre de tu estudiante: ")
        if is_valid_name(full_name):
            return full_name
        print("Nombre no válido")

def is_valid_section(section):
    return bool(re.fullmatch(r"\d{1,2}[A-Z]", section))

def get_valid_section():
    while True:
        section = input ("Seccion: ").strip().upper()

        if is_valid_section(section):
            return section

        print("Sección inválida, Use un formato válido como 10A, 11B o 9C.")

def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"{subject.replace('_', ' ').title()} grade: "))

            if 0 <= grade <= 100:
                return grade

            print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("ingrese un número, no una letra")

'''
def student_exists(students, full_name, section):
    for student in students:
        if(
            student["full_name"].lower() == full_name.lower()
            and student["section"].upper() == section.upper()
        ):
            return True
    return False


def calculate_average(student):
    total = 0

    for subject in SUBJECTS:
        total += student[subject]

    return total / len(SUBJECTS)

def add_students(students):
    while True:
        try:
            amount = int(input("¿Cuántos estudiantes deseas agregar?"))

            if amount > 0:
                break
            print("Debe ser mayor a cero")

        except ValueError:
            print("Valor inválido, favor de ingresar un digito")

    for index in range(amount):
        print(f"\nStudent #{index + 1}: ")

        full_name = get_valid_name()
        section = get_valid_section()

        if student_exists(students, full_name, section):
            print("El estudiante ya existe, y no fue agregado")
            continue
        student = {
            "full_name": full_name,
            "section": section,
            "español": get_valid_grade("español"),
            "inglés" : get_valid_grade("inglés"),
            "estudios_sociales" : get_valid_grade("estudios sociales"),
            "ciencias" : get_valid_grade("ciencias"),
        }
        students.append(student)
        print("El estudiante fue agregado de manera satisfactoria")

def show_students(students):
    if not students:
        print("No hay estudiantes registrados")
        return

    for student in students:
        print("\n----------------------")
        print(f"Nombre: {student['full_name']}")
        print(f"Seccion: {student['section']}")
        print(f"Español: {student['español']}")
        print(f"Inglés: {student['inglés']}")
        print(f"Estudios Sociales: {student['estudios_sociales']}")
        print(f"ciencias: {student['ciencias']}")
        print(f"promedio: {calculate_average(student):.2f}")

def show_top_three_students(students):
    if not students:
        print("No hay estudiantes registrados")
        return

    sorted_students = sorted(
        students,
        key=calculate_average,
        reverse=True
    )

    print("\n===== Top 3 Mejores Estudiantes =====")

    for index, student in enumerate(sorted_students[:3], start=1):
        print(
            f"{index}. {student['full_name']} - "
            f"{student['section']} - "
            f"Promedio: {calculate_average(student):.2f}"
        )


def show_general_average(students):
    if not students:
        print("No hay estudiantes registrados")
        return

    total_average = 0

    for student in students:
        total_average += calculate_average(student)

    general_average = total_average / len(students)

    print(f"Promedio General: {general_average:.2f}")


def delete_student(students):
    if not students:
        print("No hay estudiantes registrados")
        return

    full_name = get_valid_name()
    section = get_valid_section()

    for student in students:
        if (
            student["full_name"].lower() == full_name.lower()
            and student["section"].upper() == section.upper()
        ):
            confirmation = input(
                "¿Está seguro de querer eliminar a este estudiante? si/no"
            ).lower()

            if confirmation == "si":
                students.remove(student)
                print("El alumno fue eliminado de manera satisfactoria")
            else:
                print("Eliminación cancelada")

            return

    print("El estudiante no existe")

def show_failed_students(students):
    if not students:
        print("No hay estudiantes registrados")
        return

    found_failed_students = False

    print("\n===== Estudiantes Reprobados =====")

    for student in students:
        failed_subjects = []

        for subject in SUBJECTS:
            if student[subject] < 60:
                failed_subjects.append((subject, student[subject]))

        if failed_subjects:
            found_failed_students = True
            print(f"\nNombre: {student['full_name']}")
            print(f"Seccion: {student['section']}")
            print("Materias reprobadas:")

            for subject, grade in failed_subjects:
                print(f"- {subject.replace('_', ' ').title()}: {grade}")

    if not found_failed_students:
        print("No hay estudiantes reprobados.")
'''