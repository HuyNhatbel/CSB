# Trắc nghiệm: 1D 2B 3C 4A 5B 6C 7D 8D 9C 10C

# Thực hành
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

nums1 = list(map(int, input("Nhập mảng nums1: ").split()))
nums2 = list(map(int, input("Nhập mảng nums2: ").split()))

if not is_sorted(nums1):
    raise Exception("nums1 chưa được sắp xếp tăng dần")
if not is_sorted(nums2):
    raise Exception("nums2 chưa được sắp xếp tăng dần")

merged = []
for x in nums1:
    merged.append(x)
for x in nums2:
    merged.append(x)

bubble_sort(merged)

print("Mảng gộp đã sắp xếp không giảm:", merged)