def insertion_sort(list):
    for sort_len in range(1, len(list)):
        cur_item = list[sort_len]
        insert_idx = sort_len
        while insert_idx > 0 and cur_item < list[insert_idx - 1]:
            list[insert_idx], list[insert_idx - 1] = list[insert_idx - 1],  list[insert_idx]
            insert_idx += 1
        list[insert_idx] = cur_item
    return list


my_array = []

print(insertion_sort(my_array))
