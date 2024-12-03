from pathlib import Path
import re


def multiply_muls(input_str: str) -> int:
    regex = r"mul\(\d+,\d+\)"

    all_muls = re.findall(regex, input_str)

    integers = r"\d+"

    res = 0

    for mul in all_muls:
        first, second = re.findall(integers, mul)
        res += int(first) * int(second)

    return res


p = Path(__file__).with_name("input_day3.txt")

with open(p, "r") as file:
    input: str = file.read().strip()


# split_by_dont = input.split("don't()")
# first_mul_split = split_by_dont[0]
#
# split_by_does = [
#     i[1:]
#     for i in filter(lambda x: len(x) > 1, [x.split("do()") for x in split_by_dont])
# ]
#
# flat = [x for xs in split_by_does for x in xs]

first = multiply_muls(input)
print(first)
# others = sum([multiply_muls(i) for i in flat])
#
# print(first + others)
