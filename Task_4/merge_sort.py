def print_array(array):
    for i in range(len(array)):
        print(array[i], end=' ')


def merge_two_lists(list_1, list_2):
    len_1 = len(list_1)
    len_2 = len(list_2)
    e = j = k = 0
    merge_list = [0 for _ in range(len_1 + len_2)]
    while e < len_1 and j < len_2:
        if list_1[e] <= list_2[j]:
            merge_list[k] = list_1[e]
            e += 1
        else:
            merge_list[k] = list_2[j]
            j += 1
        k += 1
    while e < len_1:
        merge_list[k] = list_1[e]
        e += 1
        k += 1
    while j < len_2:
        merge_list[k] = list_2[j]
        j += 1
        k += 1
    return merge_list


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        left_part = array[:mid]
        right_part = array[mid:]
        left_part = merge_sort(left_part)
        right_part = merge_sort(right_part)
        return merge_two_lists(left_part, right_part)


n = int(input())
arr = list(map(int, input().split(" ")))
arr = merge_sort(arr)
print_array(arr)
