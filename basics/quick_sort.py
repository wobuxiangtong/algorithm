#趣图
#https://idea-instructions.com/quick-sort/

def quick_sort_1(arr):
        if len(arr) <= 1:
                return arr 
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort_1(left) + middle + quick_sort_1(right)

print(quick_sort_1([3,6,8,10,1,2,1]))

def quick_sort_2(array, l, r):  
    if l < r:  
        q = partition(array, l, r)  
        quick_sort_2(array, l, q - 1)  
        quick_sort_2(array, q + 1, r)  
  
def partition(array, l, r):  
    x = array[r]  
    i = l
    for j in range(l, r):  
        if array[j] <= x:    
            array[i], array[j] = array[j], array[i]
            i += 1  
    array[i], array[r] = array[r], array[i]  
    return i
a = [3,6,8,10,1,2,1,2,3,4,64,3,5,2,55,3]
quick_sort_2(a,0,15)
print(a)

