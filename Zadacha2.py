# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

N = int(input())
sum = 0
for i in range(N):
    sum = sum + N
    N = N - 1
print(sum)
