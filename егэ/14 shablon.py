x = 7 * 512 **120 - 6 * 64 ** 100 + 8 ** 210 - 225
s = " "
while x != 0:
    s = str(x % 8)+s
    x //= 8
print(s.count("0"))
