
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # Trả về vị trí nếu tìm thấy phần tử
        elif arr[mid] < target:
            left = mid + 1  # Tìm kiếm bên phải
        else:
            right = mid - 1  # Tìm kiếm bên trái
    
    return -1  # Trả về -1 nếu không tìm thấy

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 9

result = binary_search(arr, target)
if result != -1:
    print(f'Phần tử {target} được tìm thấy tại chỉ số {result}')
else:
    print(f'Phần tử {target} không có trong mảng')
