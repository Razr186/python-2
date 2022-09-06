# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

N = int(input())
delitel = 2
while N % delitel != 0:
    delitel += 1
print(delitel)