from actions import (
    add_students,
    show_students,
    show_top_three_students,
    show_general_average,
    delete_student,
    show_failed_students,
)
from data import export_students_to_csv, import_students_from_csv


def show_menu():
    print("\n===== Sistema de Control de Estudiantes =====")
    print("1. Agrega estudiante")
    print("2. Muestra todos los estudiantes")
    print("3. Muestra el top 3 de estudiantes")
    print("4. Muestra el promedio general")
    print("5. Exporta estudiantes a CSV")
    print("6. Imports estudiantes de un CSV")
    print("7. Borra un estudiante")
    print("8. Muestra estudiantes reprobados")
    print("9. Exit")


def get_menu_option():
    while True:
        option = input("Elige una opción: ")

        if option.isdigit() and 1 <= int(option) <= 9:
            return int(option)

        print("Opción inválida, elige un número entre 1 y 9.")


def run_menu(students):
    while True:
        show_menu()
        option = get_menu_option()

        if option == 1:
            add_students(students)
        elif option == 2:
            show_students(students)
        elif option == 3:
            show_top_three_students(students)
        elif option == 4:
            show_general_average(students)
        elif option == 5:
            export_students_to_csv(students)
        elif option == 6:
            imported_students = import_students_from_csv()
            if imported_students:
                students.clear()
                students.extend(imported_students)
        elif option == 7:
            delete_student(students)
        elif option == 8:
            show_failed_students(students)
        elif option == 9:
            print("Adiós")
            break