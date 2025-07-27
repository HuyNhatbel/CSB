def insertion_sort(arr):
    for index in range(1, len(arr)):
        insert_index = index
        current_value = arr.pop(index)
        for j in range(index, -1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value)
    return arr

color_code = {'r': 1, 'w': 2, 'b': 3}
    
def convert_color_code(color_arr):
    result = []
    for c in color_arr:
        num = color_code(c)
        result.append(num)
        
    if len(result) != len(color_arr):
        raise ValueError("Danh sách này chứa tên màu không đúng quy định (r, w, b)")
    
    return result

def convert_color_char(color_num):
    global color_code
    result = []
    for num in color_num:
        for key, value in color_code.items():
            if value == num:
                result.append(key)

    if len(result) != len(color_num):
        raise ValueError("Danh sách này chứa tên màu không đúng quy định (1, 2, 3)")
    return result

def test_drive():
    color_arr = input("Nhập danh sách (r, w, b), mỗi phần tử cách nhau bằng 1 space: ")
    try:
        color_arr = color_arr.split(" ")
        color_code_list = convert_color_code(color_arr)
        sorted_color_code_list = insertion_sort(color_code_list)
        sorted_color_char_list = convert_color_char(sorted_color_code_list)
        print(sorted_color_char_list)
    except Exception as e:
        print("Error: ", e)
    finally:
        print("End")