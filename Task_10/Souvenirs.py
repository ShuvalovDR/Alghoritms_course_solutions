def find_cheapest_souvenir(ar: list) -> int:
    index_min = 0
    for j in range(len(ar)):
        if ar[j] < ar[index_min]:
            index_min = j
    return index_min


def buy_the_biggest_amount_of_souvenirs(s: int, c: list) -> int:
    souvenirs = 0
    m = find_cheapest_souvenir(c)
    while s - c[m] >= 0 and len(c) != 0:
        s -= c[m]
        souvenirs += 1
        c.pop(m)
        m = find_cheapest_souvenir(c)
    return souvenirs


n, S = map(int, input().split(" "))
cost = [0 for _ in range(n)]
for i in range(n):
    cost[i] = int(input())

max_souvenirs = buy_the_biggest_amount_of_souvenirs(S, cost)
print(max_souvenirs)
