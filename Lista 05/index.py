import time
import random

# Função de ordenação: Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Função de ordenação: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Função de ordenação: Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Função de ordenação: Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Função de ordenação: Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Função auxiliar para imprimir um array
def print_array(arr):
    print("Array:", arr)

# Função para selecionar o algoritmo de ordenação
def select_sort_algorithm():
    value = 0
    while value == 0:
        print("Selecione o algoritmo de ordenação:")
        print("1. Selection Sort")
        print("2. Bubble Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("0. Sair")

        option = int(input("Opção: "))

        if option == 0:
            print("Encerrando o programa...")
            break
        elif option == 1:
            print("Selecionado: Selection Sort")
            arr = extended_array.copy()
            start_time = time.time()
            selection_sort(arr)
            end_time = time.time()
            execution_time = end_time - start_time
            print_array(arr)
            print(f"Tempo de execução: {execution_time:.6f} segundos")
        elif option == 2:
            print("Selecionado: Bubble Sort")
            arr = extended_array.copy()
            start_time = time.time()
            bubble_sort(arr)
            end_time = time.time()
            execution_time = end_time - start_time
            print_array(arr)
            print(f"Tempo de execução: {execution_time:.6f} segundos")
        elif option == 3:
            print("Selecionado: Insertion Sort")
            arr = extended_array.copy()
            start_time = time.time()
            insertion_sort(arr)
            end_time = time.time()
            execution_time = end_time - start_time
            print_array(arr)
            print(f"Tempo de execução: {execution_time:.6f} segundos")
        elif option == 4:
            print("Selecionado: Merge Sort")
            arr = extended_array.copy()
            start_time = time.time()
            merge_sort(arr)
            end_time = time.time()
            execution_time = end_time - start_time
            print_array(arr)
            print(f"Tempo de execução: {execution_time:.6f} segundos")
        elif option == 5:
            print("Selecionado: Quick Sort")
            arr = extended_array.copy()
            start_time = time.time()
            quick_sort(arr, 0, len(arr) - 1)
            end_time = time.time()
            execution_time = end_time - start_time
            print_array(arr)
            print(f"Tempo de execução: {execution_time:.6f} segundos")
        else:
            print("Opção inválida! Tente novamente.")

# Array original
original_array = []

# Adicionando mais 500 números ao array original
extended_array = original_array + list(range(1, 501))

# Embaralhando o array estendido
random.shuffle(extended_array)

# Chamando a função para selecionar o algoritmo de ordenação
select_sort_algorithm()
