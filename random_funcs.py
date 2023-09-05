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


def place_value(n):
    values_list = []
    if len(str(n)) < 2:
        print(f"{n} = {n} x (10^0)")
    else:
        for idx, digit in enumerate(reversed(str(n))):  # OR: str(n)[::-1]
            values_list.append(f"{digit} x 10^{idx}")

    return "\n".join(values_list)
