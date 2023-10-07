def decode(a, b, c):
    s = ''
    s += str(a + b + c)
    s += ' '
    for _ in range(c):
        s += '1 '
    for _ in range(b):
        s += '5 '
    for i in range(a):
        s += '10 '
    print(s.strip())


def count_iters(m):
    k = 0
    while m >= 0:
        k += m // 5 + 1
        m -= 10
    return k


def generate_all(a, b, c):
    decode(a, b, c)
    if c - 5 >= 0:
        generate_all(a, b + 1, c - 5)
    else:
        return

m = int(input())
print(count_iters(m))
for i in range(m // 10 + 1):
    generate_all(i, 0, m - 10 * i)
