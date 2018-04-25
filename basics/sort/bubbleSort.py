def bubble_sort(arr):
    for i in range(len(arr) -1):
        for j in range(len(arr) - 1 -i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)
print(arr)


#递归冒泡
def recursion_bubble_sort(arr,n):
    if n == 1:
        return
    for i,_ in enumerate(arr[:n-1]):
        if arr[i+1] < arr[i]:
            # print(num,arr[i],arr)
            arr[i],arr[i+1] = arr[i+1],arr[i]
    recursion_bubble_sort(arr,n-1)


listt = [64, 34, 25, 12, 22, 11, 90]
recursion_bubble_sort(listt,len(listt))
print(listt)