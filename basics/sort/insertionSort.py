def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i - 1
        key = arr[i]
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

def recursive_insert_sort(arr,i):
    if i == len(arr):
        return
    j = i - 1
    key = arr[i]
    while j >=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j + 1] = key
    recursive_insert_sort(arr,i+1)
arr = [12, 11, 13, 5, 6]
recursive_insert_sort(arr,1)
print(arr)


