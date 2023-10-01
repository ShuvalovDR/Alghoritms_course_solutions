from random import randint


def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")


def lomuto_partition(array, low, high):
    pivot = low
    j = low
    for i in range(low + 1, high + 1):
        if array[i] < array[pivot]:
            j += 1
            array[i], array[j] = array[j], array[i]
    array[j], array[pivot] = array[pivot], array[j]
    return j


def randomize_array(array, low, high):
    random_index = randint(low, high)
    array[low], array[random_index] = array[random_index], array[low]


def quick_sort(array, low, high):
    if low < high:
        randomize_array(array, low, high)
        pivot = lomuto_partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)
    return array


n = int(input())
ar = list(map(int, input().split(" ")))
ar = quick_sort(ar, 0, len(ar) - 1)
print_array(ar)
