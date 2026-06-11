def bubble_sort_right_to_left(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        # recorrer de derecha a izquierda
        for j in range(n - 1, i, -1):
            if arr[j - 1] > arr[j]:  # intercambio
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True

        # optimización: detener si ya está ordenado
        if not swapped:
            break


# prueba
x = [9, 8, 0, 5, 4, 3, 7]

bubble_sort_right_to_left(x)

print(x)
