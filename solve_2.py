list_a = []
dict_b = {}

with open("input.txt", "r") as file:
    for line in file:
        chunks = line.strip().split(" ")
        list_a.append(int(chunks[0]))

        list_b_chunk = int(chunks[-1])

        if list_b_chunk in dict_b:
            dict_b[list_b_chunk] = dict_b[list_b_chunk] + 1
        else:
            dict_b[list_b_chunk] = 1


res = 0

for i in list_a:
    if i in dict_b:
        res += i * dict_b[i]

print(res)
