import time
import random

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def test_search_methods(arr, x):
    start = time.time()
    result_linear = linear_search(arr, x)
    end = time.time()
    print(f"Linear Search: Index = {result_linear}, Time = {end - start:.6f} seconds")

    arr_sorted = sorted(arr)
    start = time.time()
    result_binary = binary_search(arr_sorted, x)
    end = time.time()
    print(f"Binary Search: Index = {result_binary}, Time = {end - start:.6f} seconds")
    print("-" * 50)


def main():
    sizes = [10**3, 10**4, 10**5, 10**6]
    for size in sizes:
        arr = list(range(size))
        x = random.choice(arr) 
        print(f"Array size: {size}, Searching for: {x}")
        test_search_methods(arr, x)


if __name__ == "__main__":
    main()
    
# Với mảng nhỏ, thời gian chênh lệch không đáng kể
# Với mảng lớn hơn(>100000), binary search thực hiện tìm kiếm nhanh hơn