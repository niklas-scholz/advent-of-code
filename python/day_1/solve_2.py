list_a = []
dict_b = {}

with open("input.txt", "r") as file:
    for row in file:
        chunks = row.strip().split(" ")
        list_a.append(int(chunks[0]))

        list_b_chunk = int(chunks[-1])

        dict_b[list_b_chunk] = dict_b.get(list_b_chunk, 0) + 1


res = 0

for i in list_a:
    if i in dict_b:
        res += i * dict_b[i]

print(res)
