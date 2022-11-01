def match(n):
    total = 1
    while n != 2:
        total += int(n / 2)
        n = round(n / 2)
    return total

print(match(7))