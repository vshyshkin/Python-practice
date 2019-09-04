def buble_sort(list):
    swapped = True
    while swapped:
        swapped = False
        buff = 0
        for i in range(0, len(list)-1):
            if list[i]>list[i+1]:
                list[i],list[i + 1] = list[i+1], list[i]
    return list

my_array = []

print(buble_sort(my_array))