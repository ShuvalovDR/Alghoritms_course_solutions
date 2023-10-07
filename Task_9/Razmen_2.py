money = int(input())
coins = [50, 20, 10, 5, 1]
return_coins = []
for i in range(len(coins)):
    return_coins.append(money // coins[i])
    money %= coins[i]
print(sum(return_coins))
s = ''
for i in range(len(return_coins)):
    for j in range(return_coins[i]):
        s += str(f'{coins[i]} ')
print(s.strip())