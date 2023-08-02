class iter_int(int):
    def __getitem__(self, idx):
        digits_str = str(self)
        
        if idx >= len(digits_str) or idx < -len(digits_str):
            raise IndexError("Index out of range")
        return int(digits_str[idx])


num = iter_int(1234567890)


print(num[0])
print(num[5])
print(num[-1])
print(num[20])