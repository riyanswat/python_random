# iterable integer
class IterInt(int):
    def __getitem__(self, idx):
        digits_str = str(self)

        if idx >= len(digits_str) or idx < -len(digits_str):
            raise IndexError("Index out of range")
        return int(digits_str[idx])


num = IterInt(1234567890)


print(num[0])
print(num[5])
print(num[-1])
print(num[20])


# ---------------------------------

# Prints the place value of a digit in a number
def place_value(n):
    values_list = []
    if len(str(n)) < 2:
        print(f"{n} = {n} x (10^0)")
    else:
        for idx, digit in enumerate(reversed(str(n))):  # OR: str(n)[::-1]
            values_list.append(f"{digit} x 10^{idx}")

    return "\n".join(values_list)


print(place_value(3567))

# ---------------------------------



import random
from collections import Counter


def random_function():
    def square(n):
        return n ** 2

    def cube(n):
        return n ** 3

    def fourth_power(n):
        return n ** 4

    funcs = [square, cube, fourth_power]

    return random.choice(funcs)


results = []
for i in range(10):
    rand_func = random_function()
    results.append(rand_func(2))


counter = Counter(results)
print(counter.most_common(1)[0][0])
