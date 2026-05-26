import re

SUBJECTS = ["spanish", "english", "social_studies", "science"]

class Student:
    def __init__(self, name, section, spanish, english, social_studies, science):
        self.name = name
        self.section = section
        self.spanish = float(spanish)
        self.english = float(english)
        self.social_studies = float(social_studies)
        self.science = float(science)


def is_valid_name(name):
    return bool(name.strip() and not any(char.isdigit() for char in name))

def get_valid_name():
    while True:
        full_name = input("Ingrese el nombre de tu estudiante: ").strip()
        if is_valid_name(full_name):
            return full_name
        print("Nombre inválido, no puede contener números")

def is_valid_section(section):
    return bool(re.fullmatch(r"\d{1,2}[A-Z]", section))

def get_valid_section():
    while True:
        section = input ("Seccion: ").strip().upper()

        if is_valid_section(section):
            return section

        print("Sección inválida, Use un formato válido como 10A, 11B o 9C.")

def student_exists(students, full_name, section):
    for student in students:
        if(
            student.name.lower() == full_name.lower()
            and student.section.upper() == section.upper()
        ):
            return True
    return False

def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"{subject.replace('_', ' ').title()} grade: "))

            if 0 <= grade <= 100:
                return grade

            print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("ingrese un número, no una letra")

def add_students(students):
    while True:
        try:
            ammount = int(input("¿Cuántos estudiantes deseas agregar?"))

            if ammount > 0:
                break
            print("Debe ser mayor a cero")

        except ValueError:
            print("Valor inválido, favor de ingresar un digito")

    for index in range(ammount):
        print(f"\nStudent #{index + 1}: ")
        name = get_valid_name()
        section = get_valid_section()

        if student_exists(students, name, section):
            print("El estudiante ya existe, y no fue agregado")
            continue
        student = Student(
            name,
            section,
            get_valid_grade("spanish"),
            get_valid_grade("english"),
            get_valid_grade("social_studies"),
            get_valid_grade("science")
        )
        students.append(student)
        print("El estudiante fue agregado de manera satisfactoria")

def calculate_average(student):
    total = 0

    for subject in SUBJECTS:
        total += getattr(student, subject)

    return total / len(SUBJECTS)

def show_students(students):
    if not students:
        print("No hay estudiantes registrados")
        return
    for student in students:
        print("\n----------------------")
        print(f"Nombre: {student.name}")
        print(f"Seccion: {student.section}")
        print(f"Español: {student.spanish}")
        print(f"Inglés: {student.english}")
        print(f"Estudios Sociales: {student.social_studies}")
        print(f"Ciencias: {student.science}")
        print(f"Promedio: ",calculate_average(student))

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
            f"Alumno No. {index}. Nombre: {student.name} - "
            f"Sección :{student.section} - "
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
            student.name.lower() == full_name.lower()
            and student.section.upper() == section.upper()
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
            subject_grade = getattr(student, subject)
            if subject_grade < 60:
                failed_subjects.append((subject, getattr(student, subject)))

        if failed_subjects:
            found_failed_students = True
            print(f"\nNombre: {student.name}")
            print(f"Seccion: {student.section}")
            print("Materias reprobadas:")

            for subject, grade in failed_subjects:
                print(f"- {subject.replace('_', ' ').title()}: {grade}")

    if not found_failed_students:
        print("No hay estudiantes reprobados.")