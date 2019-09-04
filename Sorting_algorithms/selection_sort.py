
def selection_sort(list):
    sort_len = 0
    while sort_len < len(list):
        min_idx = -1
        for i, elem in enumerate(list[sort_len:]):
            if min_idx is None or elem<list[min_idx]:
                min_idx = i+sort_len
        print(list)
        list[sort_len], list[min_idx] = list[min_idx], list[sort_len]
        sort_len += 1
    return list


my_array = []

print(selection_sort(my_array))