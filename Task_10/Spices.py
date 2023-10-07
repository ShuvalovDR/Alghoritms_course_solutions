def index_max(ar: list) -> int:
    maximum_index = 0
    for j in range(len(ar)):
        if ar[j] > ar[maximum_index]:
            maximum_index = j
    return maximum_index


def maximum_cost_of_spices(W: int, cost: list, weight: list, weight_of_unit_mass: list) -> float:
    value = 0.0
    while W != 0 and len(weight_of_unit_mass) != 0:
        m = index_max(weight_of_unit_mass)
        amount = min(W, weight[m])
        value += cost[m] / weight[m] * amount
        W -= amount
        cost.pop(m)
        weight.pop(m)
        weight_of_unit_mass.pop(m)
    return value


n, W = map(int, input().split(" "))
cost = [0 for _ in range(n)]
weight = cost.copy()
weight_of_unit_mass = cost.copy()
for i in range(n):
    c, w = map(int, input().split(" "))
    cost[i] = c
    weight[i] = w
    weight_of_unit_mass[i] = c / w
max_cost = maximum_cost_of_spices(W, cost, weight, weight_of_unit_mass)
max_cost = round(max_cost, 3)
print(max_cost)


