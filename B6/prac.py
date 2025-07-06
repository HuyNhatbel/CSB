def binary_search_loop(arr, target) -> int:
    #danh sach rong
    if not arr: return -1
    #tao mid, start, end
    start, end = 0, len(arr) -1
    mid = (end - start) // 2 + start
    while start <= end:
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        mid = (end - start) // 2 + start
    return -1
try:
    n = int(input())
    if n <= 0:
        raise ValueError("n must be a positive integer")
    arr = input().split(" ")
    if len(arr) != n:
        raise ValueError("The number of elements does not match n")
    arr = [int(x) for x in arr]
    target = int(input())
    
    arr.sort()
    result = binary_search_loop(arr, target)
    print(result)
except Exception as e:
    print("Error:", e)
finally:
    print("End.")