list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

employee = {}

for i in range(len(list_a)):
    employee[list_a[i]] = list_b[i]

print(employee)
