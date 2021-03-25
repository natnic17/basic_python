rank = [7, 5, 3, 3, 2]
x = int(input('Введите число: '))
rank.insert(0, x)
for i in range(len(rank) - 1):
    if rank[i] <= rank[i + 1]:
        rank[i], rank[i + 1] = rank[i + 1], rank[i]
print(rank)