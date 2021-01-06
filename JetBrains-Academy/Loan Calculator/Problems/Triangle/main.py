# https://hyperskill.org/learn/daily/9478
num = int(input())

for i in range(0, num):
    s_triangle = '#' * (i * 2 + 1)
    print(s_triangle.center((num - 1) * 2 + 1))
