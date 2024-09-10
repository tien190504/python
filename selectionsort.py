def selection_sort(arr):
    for i in range(len(arr)):
        minium = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minium]:
                minium = j
        arr[i], arr[minium] = arr[minium], arr[i]
    return arr
