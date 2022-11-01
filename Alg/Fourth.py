def minimumAbsDifference(arr):
    arr = sorted(arr)
    min = 2 ** 31
    result = []
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] < min:
            min = arr[i + 1] - arr[i]
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == min:
            result += [[arr[i], arr[i + 1]]]
    return(result)

print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))