reports = []

with open("input_day_2.txt", "r") as file:
    for row in file:
        reports.append([int(level) for level in row.split(" ")])


res = 0

for report in reports:
    slope = 0

    for i in range(len(report) - 1):
        cur_level = report[i]
        next_level = report[i + 1]

        diff = cur_level - next_level
        print(diff)

        if abs(diff) > 3 or abs(diff) < 1:
            break

        if diff > 0:
            if slope == 0:
                slope = -1
            elif slope == 1:
                break
        elif diff < 0:
            if slope == 0:
                slope = 1
            elif slope == -1:
                break

        if i + 1 == len(report) - 1:
            res += 1


print(res)
