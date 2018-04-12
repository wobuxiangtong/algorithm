def insert_sort(lists):
    l = len(lists)
    for i in range(1,l):
        key = lists[i]
        j = i - 1
        while j >= 0 and key < lists[j]:
            #排好序元素后移一位
            lists[j + 1] = lists[j]
            j -= 1
        #插入当前元素的下一位
        lists[j+1] = key

a = [4, 3, 8, 3, 5, 9, 5,3,6,3,7,4,8,3,53,22,44]
insert_sort(a)
print(a)
