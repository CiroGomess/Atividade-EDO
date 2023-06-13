import time
import random
import os


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


def select_input_file():
    print("Selecione o arquivo de entrada:")
    print("1. num.1000.1.in")
    print("2. num.1000.2.in")
    print("3. num.1000.3.in")
    print("4. num.1000.4.in")
    print("5. num.10000.1.in")
    print("6. num.10000.2.in")
    print("7. num.10000.3.in")
    print("8. num.10000.4.in")
    print("9. num.100000.1.in")
    print("10. num.100000.2.in")
    print("11. num.100000.3.in")
    print("12. num.100000.4.in")
    
    option = int(input("Opção: "))
    
    if option == 1:
        return "num.1000.1.in"
    elif option == 2:
        return "num.1000.2.in"
    elif option == 3:
        return "num.1000.3.in"
    elif option == 4:
        return "num.1000.4.in"
    elif option == 5:
        return "num.10000.1.in"
    elif option == 6:
        return "num.10000.2.in"
    elif option == 7:
        return "num.10000.3.in"
    elif option == 8:
        return "num.10000.4.in"
    elif option == 9:
        return "num.100000.1.in"
    elif option == 10:
        return "num.100000.2.in"
    elif option == 11:
        return "num.100000.3.in"
    elif option == 12:
        return "num.100000.4.in"
    else:
        print("Opção inválida! Tente novamente.")
        return select_input_file()



# Selecionar o arquivo de entrada
input_file = select_input_file()

# Construir o caminho completo do arquivo
file_path = os.path.join("instancias-num", input_file)


# Ler os valores do arquivo
with open(file_path, "r") as file:
    extended_array = [int(line) for line in file]

# Embaralhar o array estendido
random.shuffle(extended_array)

# Chamando a função para selecionar o algoritmo de ordenação
select_sort_algorithm()