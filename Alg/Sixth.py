def getKth(lo, hi, k):
    values = []
    power = []
    for i in range(lo, hi + 1):
        values.append(i)
    for v in values:
        counter = 0
        while v != 1:
            counter += 1
            if v % 2 == 0:
                v /= 2
            else:
                v = 3 * v + 1
        power.append(counter)
    dic = dict(zip(values, power))
    res = sorted(dic.items(), key=lambda x: (x[1],x[0]))
    return res[k - 1][0]

print(getKth(lo = 7, hi = 11, k = 4))