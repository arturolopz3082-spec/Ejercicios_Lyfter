number_of_grades = int(input("¿Cuántas notas vas a ingresar? "))

approved_count = 0
failed_count = 0
total_approved = 0
total_failed = 0
total_sum = 0

for i in range(number_of_grades):
    grade = float(input(f"Ingrese la nota {i + 1}: "))
    total_sum += grade

    if grade > 70:
        approved_count += 1
        total_approved += grade
    elif grade < 70:
        failed_count += 1
        total_failed += grade

average_total = total_sum / number_of_grades if number_of_grades > 0 else 0
average_approved = total_approved / approved_count if approved_count > 0 else 0
average_failed = total_failed / failed_count if failed_count > 0 else 0

print("\nResultados:")
print("Notas aprobadas:", approved_count)
print("Notas desaprobadas:", failed_count)
print("Promedio general:", average_total)
print("Promedio aprobadas:", average_approved)
print("Promedio desaprobadas:", average_failed)