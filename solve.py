list_a, list_b = [], []

with open("input.txt", "r") as file:
    for line in file:
        chunks = line.strip().split(" ")
        list_a.append(int(chunks[0]))
        list_b.append(int(chunks[-1]))

assert len(list_a) == len(list_b)

list_a.sort()
list_b.sort()

res = 0

for i in range(len(list_a)):
    res += abs(list_a[i] - list_b[i])

print(res)
