def bubble_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Bubble sort nada más acepta listas")
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

x = [9,8,0,5,4,3,7]

bubble_sort(x)
print(x)