n, m = map(int, input().split(' '))
n += 1
m += 1
A = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    if i % 2 == 0:
        A[i][0] = 0
    else:
        A[i][0] = 1
for i in range(m):
    if i % 2 == 0:
        A[0][i] = 0
    else:
        A[0][i] = 1
for i in range(1, n):
    for j in range(1, m):
        if A[i - 1][j - 1] == 1 and A[i - 1][j] == 1 and A[i] [j - 1] == 1:
            A[i][j] = 0
        else:
            A[i][j] = 1
if A[n - 1][m - 1] == 1:
    print('Win')
else:
    print('Loose')
