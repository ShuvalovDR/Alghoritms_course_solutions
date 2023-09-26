n, m = map(int, input().split(' '))
n += 1
m += 1
A = [[-1 for i in range(m)] for j in range(n)]
A[0][0] = 0
for i in range(n):
    for j in range(m):
        # заполнение ячеек Win
        # Если из ячейки (i, j) можно попасть в проигрыщную, она выиграшная
        if j - 1 >= 0 and A[i][j - 1] == 0 \
                or j - 2 >= 0 and A[i][j - 2] == 0 \
                or i - 1 >= 0 and A[i - 1][j] == 0 \
                or i - 2 >= 0 and A[i - 2][j] == 0 \
                or i - 2 >= 0 and j - 1 >= 0 and A[i - 2][j - 1] == 0 \
                or i - 1 >= 0 and j - 2 >= 0 and A[i - 1][j - 2] == 0:
            A[i][j] = 1
        else:
            A[i][j] = 0
if A[n - 1][m - 1] == 1:
    print('Win')
else:
    print('Loose')