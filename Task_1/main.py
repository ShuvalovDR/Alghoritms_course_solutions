def cross(a, b, c, d):
    if c < a and d < a or c > b and d > b:
        return False
    else:
        return True


def find_champ(right):
    n = len(right)
    index_min = 0
    for i in range(n):
        if right[i] < right[index_min]:
            index_min = i
    return index_min


def delete_cross(left_champ, right_champ, left, right):
    new_left = list([])
    new_right = list([])
    for i, element in enumerate(zip(left, right)):
        if not cross(left_champ, right_champ, element[0], element[1]):
            new_left.append(left[i])
            new_right.append(right[i])
    return new_left, new_right


n = int(input())
left = list([])
right = list([])

for i in range(n):
    a, b = map(int, input().split(' '))
    left.append(a)
    right.append(b)

champions = list([])

while len(left) != 0 and len(right) != 0:
    index_min = find_champ(right)
    left_champ = left.pop(index_min)
    right_champ = right.pop(index_min)
    champions.append([left_champ, right_champ])
    left, right = delete_cross(left_champ, right_champ, left, right)
print(champions)
