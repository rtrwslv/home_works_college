def jewelry(jewels, stones):
    counter = 0
    for j in jewels:
        counter += stones.count(j)
    return counter

print(jewelry(jewels = "aA", stones = "aAAbbbb"))