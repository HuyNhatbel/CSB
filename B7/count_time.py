import random
arr1 = random.sample(range(100), 10)
arr2 = random.sample(range(100), 10)

def bubble_sort(arr):
    swapped_count = 0
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped_count += 1
                print(f"Lan swap {swapped_count:02}: {arr}")
                swapped = True
        if not swapped:
            break
    return arr, swapped_count

bubble_sort(arr1)

def insertion_sort(arr):
    for index in range(1, len(arr)):
        insert_count = 0
        insert_index = index
        current_value = arr.pop(index)
        for j in range(index, -1, -1):
            if arr[j] > current_value:
                insert_index = j
                insert_count += 1
        arr.insert(insert_index, current_value)
        print(f"Lần chèn {insert_count}: {arr}")
    return arr, insert_count

arr2, insert_count = insertion_sort(arr2)
print("Arr đã sort: ", arr2)