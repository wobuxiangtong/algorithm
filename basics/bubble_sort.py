def bubble_sort(lists):
    l = len(lists)
    for i in range(0,l-1):
        for j in range(i+1,l):
            if lists[i] > lists[j]:
                lists[i],lists[j] = lists[j],lists[i]


a = [81, 23, 22, 56, 94, 47, 62, 6, 87, 17]
bubble_sort(a)
print(a)
